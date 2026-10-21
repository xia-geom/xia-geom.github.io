# AI for Math working-group page

Read `_data/ai_math_working_group.json` with the GitHub file tool before editing. It is the single record for the autumn 2026 programme and the retained reading-theme data. Both public language pages render the programme through `_includes/ai-math-programme.liquid`. Do not maintain another schedule or duplicate the news archive.

The programme transcribes an organizer-supplied example: dates and speakers are proposed, not confirmed invitations. Empty dates remain unassigned. The year is 2026. The organizer supplied session times: 09:30 on October 1 and December 3, and 12:30 on all other listed dates, including the unassigned November 5 slot. Store each time in the session’s required `time` field using 24-hour `HH:MM` format. Display speakers and their institutions, never their email addresses. No time zone, rooms, meeting links or calendar subscription have been supplied; do not infer these or generate invitations. Speaker emails and private correspondence must not enter the public repository. The validator rejects personal email fields and unknown status values. Only an explicit organizer confirmation may change programme status; a source link or AI guess does not establish a speaker’s agreement.

On October 21, 2026, the organizer requested removal of the entire Readings/Lectures section from both public pages. Do not render `_includes/ai-math-working-group.liquid`, link to that removed section, or restore its reading lists, discussion questions or session prompts without an explicit request. The existing topic records and unused include are retained without schema changes; programme themes remain plain text, not links to removed reading anchors. Read original public sources before adding resources; distinguish vendor announcements, formalization, independent checking, personal commentary and institutional statements. Do not publish Moodle links, Outlook attachment URLs or Safe Links wrappers. Link to authors’ resources rather than copying their books or private attachments. Linked institutes are resources, not claimed partners. Readings were selected from supplied topics and checked against public sources on 2026-09-30; this is not a proof audit.

`_data/ai_math_news.json` remains the only dated news record. Its updater may update that file only; it must not change the programme or reading guide. Do not advance news `last_checked` for a schedule or layout edit. A paused external updater is not a guarantee of daily publication.

The public page uses programme and news as top-level content sections. In news, use an H2 for News/Actualités, H3 headings for categories and H4 headings for individual stories. Browse by topic/Par thème and Latest notes/Dernières notes are compact navigation labels, not peer section headings. Preserve existing news permalinks, source notes and source-check dates when changing the layout. The participation invitation replaces the former provisional-programme notice; do not restore that notice.

Validate before publishing:

```sh
ruby _plugins/ai_math_working_group.rb _data/ai_math_working_group.json
ruby bin/test_ai_math_working_group.rb
```

The schema guard also runs during Jekyll’s build. Inspect the generated bilingual pages, anchors, mobile table, disclosures and privacy exclusions. Use the existing PR/build/merge workflow without bypassing failed checks. A future shared calendar should replace the date record as the source of truth and generate the public view, not create a second editable schedule. Email delivery and subscriptions require a separately authorized service; this change implements neither.
