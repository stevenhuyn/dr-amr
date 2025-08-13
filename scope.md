| Section | Details |
|---------|---------|
| Project Title | Tracking ASEAN Drug Registry Policies |
| Partner | Garrett Ehinger / Reservoir Biosecurity Consulting |
| Region of Impact | ASEAN countries |
| Problem | Policies regulating the drug registration pipeline in ASEAN countries are highly inconsistent, hampering efforts to introduce new antimicrobials in a timely manner |
| Main Objective | Develop a tool to track the drug registration policy landscape in ASEAN countries by combining LLMs and web scraping |
| Key Deliverables | 1. Completed policy table for all ASEAN countries<br>2. Reusable open source tool/repo to convert policy-region input into a binary implementation table<br>3. Public-facing write-up explaining the project and key lessons learned |
| In Scope | - Collecting and coding regulatory policy data from ASEAN national regulatory authorities (NRAs)<br>- Building spreadsheet and tool to track binary implementation<br>- Summarizing project insights in an accessible write-up |
| Out of Scope | - Formal verification with national regulatory agencies<br>- Legal interpretation of policy language<br>- Identifying gaps in ASEAN drug registration policy landscape |
| Timeline | 6 weeks (Aug 11 – Sep 22) |
| Risks & Mitigation | Risk: Policy documents may be vague, outdated, or inconsistent across countries<br>Mitigation: Use multiple sources and triangulate information; apply structured prompts and review for consistency across LLM outputs<br><br>Risk: Relevant information may be stored in extremely long documents that exceed the context window for the chosen LLM<br>Mitigation: Apply LLM-assisted key word searches, write functions to break long text into multiple prompts, use LLMs to store information in intermediate format (e.g. dataframe) for later reference<br><br>Risk: Certain documents may be challenging to web scrape or require a large amount of hard coding to access<br>Mitigation: Identify key websites and platforms used by NRAs to directly access for scraping, write conditional logic to scrape different types of documents (e.g. PDF vs. website) |
| Assumptions | - Official documents or trusted secondary sources are available online<br>- Binary policy implementation can be reasonably inferred from available texts<br>- LLM outputs can be validated through spot checks or expert review |
| Constraints | - No direct access to government databases<br>- Limited translation capacity for non-English regulatory documents<br>- Tool should be reasonably accessible to non-technical audiences (e.g. can run through CLI) |
| Theory of Change | Track ASEAN drug regulatory policies → Identify gaps in regulatory pathways → Enable targeted advocacy → Achieve policy change → Improve access to antimicrobials → Increase resilience to AMR → Save lives |
| Baseline Comparison | Manual compilation of drug registration policies (large time investment, not scalable) |