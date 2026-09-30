# AI for Math working-group page

Read `_data/ai_math_working_group.json` with the GitHub file tool before editing. It is the single public record for the six reading themes and the provisional autumn 2026 programme. Both languages render it through `_includes/ai-math-working-group.liquid` and `_includes/ai-math-programme.liquid`. Do not maintain another schedule or duplicate the news archive.

The programme transcribes an organizer-supplied example: dates and speakers are proposed, not confirmed invitations. Empty dates remain unassigned. The year is 2026; no times, rooms, meeting links or calendar subscription have been supplied. Do not infer these or generate invitations from date-only entries. Speaker emails and private correspondence must not enter the public repository. The validator rejects personal email fields and unknown status values. Only an explicit organizer confirmation may change programme status; a source link or AI guess does not establish a speaker’s agreement.

Questions and session ideas are discussion proposals, not a departmental position. Read original public sources before adding resources; distinguish vendor announcements, formalization, independent checking, personal commentary and institutional statements. Do not publish Moodle links, Outlook attachment URLs or Safe Links wrappers. Link to authors’ resources rather than copying their books or private attachments. Linked institutes are resources, not claimed partners. Readings were selected from supplied topics and checked against public sources on 2026-09-30; this is not a proof audit.

`_data/ai_math_news.json` remains the only dated news record. Its updater may update that file only; it must not change the programme or reading guide. Do not advance news `last_checked` for a schedule or layout edit. A paused external updater is not a guarantee of daily publication.

Validate before publishing:

```sh
ruby _plugins/ai_math_working_group.rb _data/ai_math_working_group.json
ruby bin/test_ai_math_working_group.rb
```

The schema guard also runs during Jekyll’s build. Inspect the generated bilingual pages, anchors, mobile table, disclosures and privacy exclusions. Use the existing PR/build/merge workflow without bypassing failed checks. A future shared calendar should replace the date record as the source of truth and generate the public view, not create a second editable schedule. Email delivery and subscriptions require a separately authorized service; this change implements neither.
