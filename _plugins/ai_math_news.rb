# Validate the one canonical news file before Jekyll can publish it.
# This checks structure and provenance fields, not mathematical correctness.
require 'date'
require 'json'
require 'uri'

module AiMathNews
  CATEGORIES = %w[research formalization benchmarks community].freeze

  def self.text(value, label, max_length = 900)
    unless value.is_a?(String) && !value.strip.empty? && value.length <= max_length && !value.match?(/[<>]/)
      raise ArgumentError, "#{label}: expected nonempty plain text (max #{max_length} characters)"
    end
  end

  def self.iso_date(value)
    raise ArgumentError, 'Expected an ISO date string' unless value.is_a?(String) && value.match?(/\A\d{4}-\d{2}-\d{2}\z/)
    Date.iso8601(value)
  end

  def self.validate(data, today: Date.today)
    raise ArgumentError, 'News must be an object' unless data.is_a?(Hash)
    checked = iso_date(data.fetch('last_checked'))
    raise ArgumentError, 'Future check date' if checked > today
    entries = data.fetch('entries')
    raise ArgumentError, 'Expected 1 to 40 entries' unless entries.is_a?(Array) && (1..40).cover?(entries.size)
    ids = []
    primary_urls = []
    entries.each do |item|
      raise ArgumentError, 'Entry must be an object' unless item.is_a?(Hash)
      id = item.fetch('id')
      raise ArgumentError, 'Invalid or duplicate ID' unless id.is_a?(String) && id.match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\z/) && !ids.include?(id)
      ids << id
      raise ArgumentError, "#{id}: unknown category" unless CATEGORIES.include?(item.fetch('category'))
      raise ArgumentError, "#{id}: publication date after source check" if iso_date(item.fetch('date')) > checked
      text(item.fetch('author'), "#{id}: author", 300)
      %w[title summary status].each do |key|
        value = item.fetch(key)
        raise ArgumentError, "#{id}: #{key} must contain en and fr" unless value.is_a?(Hash)
        %w[en fr].each { |lang| text(value.fetch(lang), "#{id}: #{key}.#{lang}") }
      end
      if item.key?('event_start') || item.key?('event_end')
        first = iso_date(item.fetch('event_start'))
        last = iso_date(item.fetch('event_end'))
        raise ArgumentError, "#{id}: reversed event dates" if last < first
      end
      sources = item.fetch('sources')
      raise ArgumentError, "#{id}: missing sources" unless sources.is_a?(Array) && (1..4).cover?(sources.size)
      urls = sources.map do |source|
        text(source.fetch('label'), "#{id}: source label", 150)
        raw = source.fetch('url')
        text(raw, "#{id}: source URL", 1000)
        url = URI.parse(raw)
        unless url.is_a?(URI::HTTPS) && url.host && !url.userinfo && !url.host.match?(/\A(?:localhost|127\.|10\.|192\.168\.)/)
          raise ArgumentError, "#{id}: expected public HTTPS source"
        end
        "#{url.host.downcase}#{url.path.sub(%r{/$}, '')}"
      end
      raise ArgumentError, "#{id}: duplicate source" unless urls.uniq == urls
      raise ArgumentError, "#{id}: duplicate primary story" if primary_urls.include?(urls.first)
      primary_urls << urls.first
    end
    true
  end
end

if defined?(Jekyll::Hooks)
  Jekyll::Hooks.register :site, :post_read do |site|
    AiMathNews.validate(site.data.fetch('ai_math_news'))
  end
end

if $PROGRAM_NAME == __FILE__
  AiMathNews.validate(JSON.parse(File.read(ARGV.fetch(0))))
  puts 'AI for Math data: valid'
end
