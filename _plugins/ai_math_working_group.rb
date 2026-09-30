# Validate the public reading guide and organizer-supplied programme before publishing.
# No fetching, invitations or calendar writes. This is not a source/proof audit.
require 'date'
require 'json'
require 'uri'

module AiMathWorkingGroup
  TOPICS = %w[research education community environment epistemology foundations].freeze

  def self.object(value, required, optional = [])
    raise ArgumentError, 'Expected an object' unless value.is_a?(Hash)
    unless (required - value.keys).empty? && (value.keys - required - optional).empty?
      raise ArgumentError, 'Missing or unrecognized fields'
    end
  end

  def self.text(value)
    unless value.is_a?(String) && !value.strip.empty? && value.length <= 1000 && !value.match?(/[<>@]/)
      raise ArgumentError, 'Expected nonempty plain text, without email addresses'
    end
  end

  def self.bilingual(value)
    object(value, %w[en fr])
    value.each_value { |string| text(string) }
  end

  def self.public_url(value)
    text(value)
    url = URI.parse(value)
    unless url.is_a?(URI::HTTPS) && url.host && !url.userinfo
      raise ArgumentError, 'Expected public HTTPS resource URL'
    end
    if value.match?(/outlook|safelinks|ena01|attachmentid|itemid|localhost|127\.0\.0\.1/i)
      raise ArgumentError, 'Private or wrapped link must not be published'
    end
  end

  def self.validate(data)
    object(data, %w[programme topics])
    topics = data.fetch('topics')
    raise ArgumentError, 'Expected the six reading themes' unless topics.is_a?(Array) && topics.size == TOPICS.size
    ids = topics.map do |topic|
      object(topic, %w[id title focus questions resources session], %w[networks])
      %w[title focus session].each { |key| bilingual(topic.fetch(key)) }
      questions = topic.fetch('questions')
      raise ArgumentError, 'Expected 1 to 6 questions' unless questions.is_a?(Array) && (1..6).cover?(questions.size)
      questions.each { |q| bilingual(q) }
      resources = topic.fetch('resources')
      raise ArgumentError, 'Expected 1 to 8 readings' unless resources.is_a?(Array) && (1..8).cover?(resources.size)
      resources.each do |resource|
        object(resource, %w[title note url])
        %w[title note].each { |key| bilingual(resource.fetch(key)) }
        public_url(resource.fetch('url'))
      end
      networks = topic.fetch('networks', [])
      raise ArgumentError, 'Networks must be a list' unless networks.is_a?(Array)
      networks.each do |network|
        object(network, %w[label url])
        text(network.fetch('label'))
        public_url(network.fetch('url'))
      end
      topic.fetch('id')
    end
    raise ArgumentError, 'Unknown or duplicate theme ID' unless ids.sort == TOPICS.sort
    programme = data.fetch('programme')
    object(programme, %w[year status sessions])
    year = programme.fetch('year')
    raise ArgumentError, 'Invalid programme year' unless year.is_a?(Integer) && (2000..2100).cover?(year)
    raise ArgumentError, 'Unsupported programme status' unless %w[provisional confirmed].include?(programme.fetch('status'))
    sessions = programme.fetch('sessions')
    raise ArgumentError, 'Expected 1 to 52 sessions' unless sessions.is_a?(Array) && (1..52).cover?(sessions.size)
    dates = sessions.map do |session|
      object(session, %w[date speaker affiliation theme])
      raw = session.fetch('date')
      raise ArgumentError, 'Expected ISO session date' unless raw.is_a?(String) && raw.match?(/\A\d{4}-\d{2}-\d{2}\z/)
      date = Date.iso8601(raw)
      raise ArgumentError, 'Session outside programme year' unless date.year == year
      %w[speaker affiliation].each { |key| text(session.fetch(key)) unless session.fetch(key).nil? }
      theme = session.fetch('theme')
      raise ArgumentError, 'Unknown session theme' unless theme.nil? || ids.include?(theme)
      if session.fetch('speaker').nil? && (!session.fetch('affiliation').nil? || !theme.nil?)
        raise ArgumentError, 'Unassigned session must not invent an affiliation or theme'
      end
      raw
    end
    raise ArgumentError, 'Duplicate or unordered session dates' unless dates == dates.uniq.sort
    true
  end
end

if defined?(Jekyll::Hooks)
  Jekyll::Hooks.register :site, :post_read do |site|
    AiMathWorkingGroup.validate(site.data.fetch('ai_math_working_group'))
  end
end

if $PROGRAM_NAME == __FILE__
  AiMathWorkingGroup.validate(JSON.parse(File.read(ARGV.fetch(0))))
  puts 'AI for Math working-group data: valid'
end
