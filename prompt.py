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
4. It should define technical terms using the provided definitions when applicable
5. It should specify searching official government sources, national regulatory authority websites, and pharmaceutical regulations

INPUT FORMAT:
- Country: [COUNTRY]
- Indicator category path and specific indicator: [INDICATOR]

TEMPLATE FOR YOUR OUTPUT:
Generate a prompt following this structure:

"Research whether [COUNTRY] [SPECIFIC POLICY REQUIREMENT]. 

Definitions for reference:
[Include only relevant definitions from the provided list]

Please determine:
1. Implementation status: Yes (fully implemented) / No (not implemented) / Partial (partially implemented) / Unknown (insufficient information)
2. Supporting evidence: Specific regulations, decrees, or official guidelines that establish this requirement
3. Implementation details: When it was implemented, any exceptions or special conditions
4. Verification: Cross-reference multiple sources if possible

Search priority:
- Official websites of [COUNTRY]'s National Regulatory Authority for pharmaceuticals
- [COUNTRY]'s Ministry of Health pharmaceutical regulations
- ASEAN PPWG documents mentioning [COUNTRY]
- WHO or PIC/S databases if relevant
- Recent pharmaceutical industry reports or regulatory updates for [COUNTRY]

Provide a concise summary with the determination first, followed by supporting details."

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

Search priority:
- Official websites of Vietnam's Drug Administration (DAV) and Ministry of Health
- Vietnamese pharmaceutical regulations and circulars (especially Circular 32/2018/TT-BYT and updates)
- ASEAN PPWG documents mentioning Vietnam
- WHO or PIC/S databases if relevant
- Recent pharmaceutical industry reports or regulatory updates for Vietnam

Provide a concise summary with the determination first, followed by supporting details."

NOW GENERATE THE RESEARCH PROMPT FOR:
Country: {{country}}
Indicator: {{indicator}}
"""