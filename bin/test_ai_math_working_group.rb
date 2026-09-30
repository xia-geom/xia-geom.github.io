require 'minitest/autorun'
require_relative '../_plugins/ai_math_working_group'

class AiMathWorkingGroupTest < Minitest::Test
  def setup
    @data = JSON.parse(File.read(File.expand_path('../_data/ai_math_working_group.json', __dir__)))
  end

  def test_published_data
    assert AiMathWorkingGroup.validate(@data)
  end

  def test_unassigned_session_allowed
    @data['programme']['sessions'][0].merge!('speaker' => nil, 'affiliation' => nil, 'theme' => nil)
    assert AiMathWorkingGroup.validate(@data)
  end

  def test_email_rejected
    @data['programme']['sessions'][0]['speaker'] = 'person@example.org'
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_unknown_field_rejected
    @data['programme']['sessions'][0]['email'] = 'person@example.org'
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_invalid_date_rejected
    @data['programme']['sessions'][0]['date'] = '2026-02-30'
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_duplicate_date_rejected
    @data['programme']['sessions'][1]['date'] = @data['programme']['sessions'][0]['date']
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_wrong_year_rejected
    @data['programme']['year'] = 2027
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_unknown_status_rejected
    @data['programme']['status'] = 'unknown'
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_missing_translation_rejected
    @data['topics'][0]['title'].delete('fr')
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_unknown_theme_rejected
    @data['programme']['sessions'][0]['theme'] = 'missing'
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_private_link_rejected
    @data['topics'][0]['resources'][0]['url'] = 'https://outlook.office365.com/owa/?AttachmentId=private'
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end

  def test_html_rejected
    @data['topics'][0]['focus']['fr'] = '<script>bad()</script>'
    assert_raises(ArgumentError) { AiMathWorkingGroup.validate(@data) }
  end
end
