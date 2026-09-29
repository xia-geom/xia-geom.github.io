# Dependency-free regression checks for the publication guard.
require_relative '../_plugins/ai_math_news'

# Fixed invented records keep negative tests independent of the changing news feed.
today = Date.iso8601('2026-01-02')
source = {
  'last_checked' => today.iso8601,
  'entries' => (1..2).map do |number|
    {
      'id' => "invented-#{number}", 'date' => '2026-01-01',
      'category' => 'community', 'author' => 'Invented author',
      'title' => { 'en' => 'Invented title', 'fr' => 'Titre fictif' },
      'summary' => { 'en' => 'Invented summary.', 'fr' => 'Résumé fictif.' },
      'status' => { 'en' => 'Synthetic test only.', 'fr' => 'Test fictif uniquement.' },
      'sources' => [{ 'label' => 'Example', 'url' => "https://example.org/story-#{number}" }],
      'event_start' => '2026-02-01', 'event_end' => '2026-02-02'
    }
  end
}
AiMathNews.validate(source, today: today)
checks = {
  'duplicate ID' => ->(d) { d['entries'] << Marshal.load(Marshal.dump(d['entries'].first)) },
  'missing French' => ->(d) { d['entries'].first['summary'].delete('fr') },
  'empty status' => ->(d) { d['entries'].first['status']['en'] = '' },
  'unknown category' => ->(d) { d['entries'].first['category'] = 'hype' },
  'future check' => ->(d) { d['last_checked'] = (today + 1).iso8601 },
  'future article' => ->(d) { d['entries'].first['date'] = (today + 1).iso8601 },
  'missing source' => ->(d) { d['entries'].first['sources'] = [] },
  'unsafe source' => ->(d) { d['entries'].first['sources'].first['url'] = 'javascript:alert(1)' },
  'HTML injection' => ->(d) { d['entries'].first['summary']['en'] = '<script>bad</script>' },
  'duplicate story' => ->(d) { d['entries'][1]['sources'] = d['entries'].first['sources'] },
  'reversed event dates' => ->(d) { d['entries'].first['event_start'] = '2026-02-03' }
}
checks.each do |label, mutate|
  copy = Marshal.load(Marshal.dump(source))
  mutate.call(copy)
  begin
    AiMathNews.validate(copy, today: today)
  rescue ArgumentError, KeyError, URI::InvalidURIError
    next
  end
  raise "Validation accepted #{label}"
end
puts "#{checks.size + 1} AI for Math validation checks passed"
