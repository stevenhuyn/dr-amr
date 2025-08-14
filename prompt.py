GEN_RESEARCH_PROMPT = """
You are generating a research prompt for investigating pharmaceutical regulatory compliance in ASEAN countries.

CONTEXT:
This is part of a project tracking ASEAN drug registry policies to identify regulatory gaps and improve antimicrobial access. We need to determine whether specific countries have implemented particular regulatory indicators.

YOUR TASK:
Generate a single, comprehensive research prompt for a Deep Research Agent (like Claude Deep Research or Perplexity Sonar Deep Research) to investigate whether a given country fulfills a specific regulatory policy indicator.

REQUIREMENTS FOR YOUR GENERATED PROMPT:
1. The prompt must be self-contained and require no follow-up clarifications
2. It should request a clear determination: Yes/No/Partial/Unknown
3. It should ask for official sources, regulatory references, and implementation dates
4. It should specify searching official government sources, national regulatory authority websites, and pharmaceutical regulations

REFERENCES:
- ASEAN Key Documents and Publications: https://asean.org/our-communities/economic-community/standard-and-conformance/key-documents-publications/
- ASEAN Agreements and Declarations: https://asean.org/our-communities/economic-community/standard-and-conformance/agreements-and-declarations/
- For Indonesia specifically:
  - BPOM Latest News: https://www.pom.go.id/berita
  - BPOM Press Release: https://www.pom.go.id/siaran-pers
  - Indonesian Food and Drug Monitoring Agency Legal Documentation: https://jdih.pom.go.id/

INPUT FORMAT:
- Country: [COUNTRY]
- Indicator category path and specific indicator: [INDICATOR]

TEMPLATE FOR YOUR OUTPUT:
Generate a prompt following this structure:

"Research whether [COUNTRY] [SPECIFIC POLICY REQUIREMENT]. 

Please determine:
1. Implementation status: Yes (fully implemented) / No (not implemented) / Partial (partially implemented) / Unknown (insufficient information)
2. Supporting evidence: Specific regulations, decrees, or official guidelines that establish this requirement
3. Implementation details: When it was implemented, any exceptions or special conditions
4. Verification: Cross-reference multiple sources if possible

Provide a concise summary with the determination first, followed by supporting details.

Useful References:
[RELEVANT REFERENCES]
"

EXAMPLE INPUT:
Country: Vietnam
Indicator: Regulatory Indicators > Technical Dossier Standards > CTD/ACTD Adoption > Mandates ACTD (for generics)

EXAMPLE OUTPUT:
"Research whether Vietnam mandates ACTD (ASEAN Common Technical Dossier) format for generic drug applications.

Please determine:
1. Implementation status: Yes (fully implemented) / No (not implemented) / Partial (partially implemented) / Unknown (insufficient information)
2. Supporting evidence: Specific regulations, decrees, or official guidelines that establish this requirement
3. Implementation details: When it was implemented, any exceptions or special conditions
4. Verification: Cross-reference multiple sources if possible

Provide a concise summary with the determination first, followed by supporting details.

Useful References
- ASEAN Key Documents and Publications: https://asean.org/our-communities/economic-community/standard-and-conformance/key-documents-publications/
- ASEAN Agreements and Declarations: https://asean.org/our-communities/economic-community/standard-and-conformance/agreements-and-declarations/"

NOW GENERATE THE RESEARCH PROMPT FOR:
Country: {country}
Indicator: {indicator}
"""

SUMMARIZE_REPORT_PROMPT = """Based on the following pharmaceutical regulatory research report, determine the implementation status and return ONLY one of these four words: Yes, No, Partial, or Unknown.

Guidelines:
- Yes: Fully implemented/accepted/mandated
- No: Not implemented/not accepted/no evidence
- Partial: Partially implemented/conditionally accepted/with exceptions
- Unknown: Insufficient information to determine

Research Report:
{content}

Return only the single word determination:"""
