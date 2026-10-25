# Grouping design v3, Step 0b — the fixed lists (October 25, 2026)

**Status:** CANDIDATE. Drafted by the Systems Engine from the pool's event questions; becomes fixed when the Founder commits this file, after which none of it may change once Step 1 starts (v3, Step 0b). Tier 3. Carries three of the five Step 0b items: the driver list (item 1), the title normalisation rule's word list (item 2), and the worked examples (item 5). The agreement threshold (item 3, 0.80) and the split conditions (item 4) are already in `founder_inputs/2026-10-25_grouping_design_v3.md`.

**Context Declaration (made before writing).** Known: design v3; the pool file's keys; the question text of every pool event, printed on the host (command in section 5). Unknown: the `description` field of any event (not printed); the outcome of any market (deliberately never printed). Missing context affects correctness? No for the lists below, which are written against question text only; the descriptions are read at Step 3 by the sorters, not here.

**What this file does not do.** It does not assign any event to any driver or group. The Systems Engine necessarily read the questions to write the driver list; its own first-read impressions are not recorded anywhere, so neither sorter can inherit them. Event ids and question texts are not listed beside any driver.

**Observation recorded at Step 0b.** The pool file holds 292 events, not 291: one event (the "next Prime Minister of Sweden" pair) has only STILL_OPEN markets and carries no resolved market, so the resolved pool spans 291 events, as the handoffs say. Both figures are correct; the sorters' list holds 292 events and the two open markets are flagged as not in the confirmatory sample.

---

## 1. Driver list (closed) — for Step 3 tagging and the Step 5 sensitivity partition

How to use: for each event, a sorter assigns every driver whose test the event passes, or `none`. Tests are applied to the question text and the event description. A driver written `Dnn-<X>` takes a parameter copied from the question (a country, a state, a city, a bank); write the parameter exactly as the question names it. Multiple drivers on one event are allowed and expected. A driver is a *shared cause*, broader than a group; passing the same driver test never by itself puts two events in one primary group.

| Id | Driver | Membership test (one line) |
|---|---|---|
| D01 | US–Iran conflict and negotiations, 2026 | The outcome depends on hostilities, ceasefire or negotiation between Iran and the US, Israel or a Gulf state; on shipping or control in the Strait of Hormuz; on Iranian leadership, sanctions, or the rial; or on Iran's participation or exclusion from an international event. |
| D02 | Yemen / Red Sea conflict, 2026 | The outcome depends on fighting or a ceasefire involving the Houthis, Saudi Arabia or Israel in or over Yemen. |
| D03 | Russia–Ukraine war: front line and peace process | The outcome depends on territorial control in Ukraine, on Russia–Ukraine negotiations, or on a meeting, call or clash whose stated subject is that war (including NATO–Russia and Trump–Putin/Zelenskyy contacts about it). |
| D04 | Russian domestic politics, 2026 | The outcome is a Russian federal, regional or local election result, or the tenure of a Russian office-holder. |
| D05 | US Federal Reserve, 2026 | The outcome is a Federal Reserve rate decision, dissent, or sequence of decisions, or the tenure of the Fed Chair. |
| D06 | US macroeconomic statistics, 2026 | The outcome is a published US statistic (inflation, unemployment, GDP) for a stated period. If the question names no country, the description decides; if neither does, the event is unresolved. |
| D07-<country> | National statistical release, by country | The outcome is a published statistic of the named country for a stated period (GDP, inflation, unemployment). One driver per country. |
| D08-<bank> | Central-bank decision, by bank (not the Fed) | The outcome is a rate decision of the named central bank. One driver per bank. |
| D09-<state> | US 2026 primaries and nominations, by state | The outcome is decided by a 2026 party primary, primary runoff, caucus or nomination contest in the named US state or territory, for any office. One driver per state. |
| D10-<city> | US or Canadian municipal election, by city | The outcome is decided by the named city's 2026 mayoral or council election or its party nomination for it. One driver per city. |
| D11 | Trump's public statements and posts | The outcome is determined by what Donald Trump posts, says, praises or insults, in a stated window. |
| D12 | Trump's travel and meetings | The outcome is whether Donald Trump attends, visits, meets or speaks with a named person, event or country in a stated window. |
| D13 | Trump administration appointments and tenure | The outcome is an appointment to, departure from, or continuation in a US federal office, including the presidency. |
| D14 | US–China trade and tariffs, 2026 | The outcome depends on US–China trade measures, purchases or tariff agreements. |
| D15 | Brazil 2026 general election | The outcome is decided by Brazil's 2026 presidential, Senate or state elections, or a party's nomination for them. |
| D16 | Colombia 2026 presidential election | The outcome is decided by Colombia's 2026 presidential election, either round. |
| D17 | Peru 2026 presidential election | The outcome is decided by Peru's 2026 presidential election, either round. |
| D18 | South Korea June 3, 2026 local elections and by-elections | The outcome is decided by the South Korean elections held on June 3, 2026. |
| D19 | UK May 2026 local and mayoral elections | The outcome is decided by the United Kingdom local, council or mayoral elections held in May 2026. |
| D20 | UK Westminster by-elections and Labour leadership, 2026 | The outcome is decided by a 2026 UK parliamentary by-election or by the Labour Party's leadership process. |
| D21 | German 2026 state (Landtag) elections | The outcome is decided by a German state parliamentary election held in 2026. |
| D22 | Andalusia 2026 regional election | The outcome is decided by the 2026 Andalusian regional election or the government it produces. |
| D23 | Sweden 2026 general election | The outcome is decided by Sweden's 2026 parliamentary election or the government it produces. |
| D24 | Malta 2026 general election | The outcome is decided by Malta's 2026 general election. |
| D25 | Latvia 2026 parliamentary election | The outcome is decided by Latvia's 2026 parliamentary election. |
| D26 | Romania government formation, 2026 | The outcome is who becomes, or when someone becomes, Romania's Prime Minister. |
| D27 | China–Taiwan military action | The outcome is whether China invades or blockades Taiwan in a stated window. |
| D28 | Israel–Hamas ceasefire | The outcome depends on the state of the Israel–Hamas ceasefire. |
| D29 | Quebec 2026 general election | The outcome is decided by Quebec's 2026 general election. |
| D30 | British Columbia politics, 2026 | The outcome is decided by a 2026 election or party leadership contest in British Columbia. |
| D31-<country> | Other national or regional election, by country | The outcome is decided by a 2026 election in a country not named above (one driver per country), including presidential, parliamentary, regional, mayoral and leadership contests there. |
| none | — | No test above applies, or the outcome is a sports result, an entertainment vote, a corporate figure, a referendum not tied to an election above, or a personal-life event of a named individual. |

Notes on grain, so the Founder can judge the list: D01, D03, D09 (summed over states), D15, D05, D06 and D11 are the broad drivers; on a first read each of the first two would touch dozens of events. That is intended: the sensitivity partition exists to show what happens if those shocks are treated as one block, and its count is reported beside the primary count, never in place of it (v3, Step 4). Two deliberate omissions: there is no "Trump" driver and no "US politics" driver, because "same topic" is not a shared cause; the three Trump drivers (D11, D12, D13) are three different processes. There is no "geopolitics" driver for the same reason.

## 2. Title normalisation — the leading-word list (Step 0b, item 2)

Normalisation, applied in this order to the event title for sorting only: (1) lower-case; (2) remove every character that is not a letter, a digit or a space (punctuation, question marks, quotation marks and dashes are removed; the "x" some titles use between two parties is a letter and stays); (3) collapse runs of spaces to one and trim; (4) remove leading words, repeatedly, while the first word is in the list **{will, the, a, an}**. No stemming, no transliteration (accented letters stay as they are), no keyword extraction, no similarity score. Reason for the list: nearly every title in the pool begins "Will …", often "Will the …"; the rest begin with a proper noun. Sort keys in order: `resolutionSource`, `eventDate`, normalised title; missing values last; tie-break `conditionId` of the event's first market. The contract in v3 Step 0b item 2 governs.

## 3. Worked examples (Step 0b, item 5) — synthetic, modelled on shapes that occur in the pool

Names below are invented so that no real event is pre-decided. Each example names the clause of the definition it exercises.

**Example A — mandatory join.** Event 1: "Will Party X win the most seats in the 2026 Ruritanian parliamentary election?" Event 2: "Will Party X win between 30 and 34 seats in the 2026 Ruritanian parliamentary election?" Same proceeding, same election day, same count: clause (a); also clause (b), since a seat band of 30–34 restricts whether "most seats" is possible given the chamber size. Log line names the shared fact ("2026 Ruritanian parliamentary election result"), the outcome window (election day as written in the resolution conditions), and the source text (the two descriptions). Decision: one group. Driver tag: D31-Ruritania on both.

**Example B — justified separation, same driver.** Event 3: "Will the Bank of Ruritania cut its key rate at the June meeting?" Event 4: "Will Ruritania's May unemployment rate be 4.3%?" Both are about Ruritania's economy in spring 2026; a sorter might feel they move together. No clause applies: not the same proceeding (a rate meeting versus a statistical release), neither outcome restricts the other (b), and they are not the same measurement over overlapping windows (c). Decision: two groups. Driver tags: D08-Bank of Ruritania on Event 3; D07-Ruritania on Event 4. The log line for each names the other as a cross-list neighbour considered and the reason for not joining. This is the shape that separates a *group* (same fact) from a *driver* (same economy).

**Example C — clause (c), and an unresolved case.** Event 5: "Will annual inflation be 3.7% in May?" Event 6: "Will annual inflation be 3.8% in June?" Event 7: "Will monthly inflation decrease by 0.6% in July?" Events 5 and 6: the same named measurement (year-over-year inflation) over outcome windows that overlap by eleven months, as the resolution conditions define them: clause (c); one group. Event 7: a different measurement (month-over-month) over a window that overlaps neither: not clause (c); separate group, same driver. **Unresolved variant:** if an event's question names no country and its description does not either, the outcome window cannot be read from the resolution conditions; the sorter marks it unresolved (v3 Step 3), and it is excluded at Step 4. The pool contains inflation questions that name no country in the title; the sorters read the description before deciding.

## 4. Still open at Step 0b

The split conditions and the threshold are in design v3. Whether the Founder wants fewer or more drivers at the broad end (D01, D03, D09, D15): fewer risks missing a real shock; more risks the sensitivity partition collapsing into a few blocks, which Gemini named as a false-FAIL mechanism. Either way the list is fixed before Step 1 and reported with its block count at Step 4.

## 5. Reproducer

The questions this file was written from were printed on the host on October 25 with, from the repo root: `python3 -c 'import json, collections; d = json.load(open("scratch/pool_resolutions_2026-10-25.json")); ev = collections.OrderedDict(); [ev.setdefault(m["event_id"], []).append(m) for m in sorted(d["markets"], key=lambda m: (str(m["event_id"]), m["conditionId"]))]; print(len(ev), "events"); [print(i, e, len(ms), str(min(str(m["first_seen"]) for m in ms))[:10], ms[0]["question"]) for i, (e, ms) in enumerate(ev.items(), 1)]'` — prints `292 events` and 292 lines; no outcome or price is printed. `grep -c "STILL_OPEN" scratch/pool_resolutions_2026-10-25.json` returns at least 2.
