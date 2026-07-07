import re

from jd_parser.utils.knowledge_base import (
    TECHNICAL_SKILLS,
    FUNCTIONAL_SKILLS,
    SOFT_SKILLS
)


def _ocr_tolerant_pattern(term):
    escaped = [re.escape(char) for char in term]
    return r"\b" + r"[\s\.\-]*".join(escaped) + r"\b"


TECHNICAL_SKILL_PATTERNS = [
    ("Programming", [r"\bProgramming\b"]),
    ("Python", [r"\bPython\b"]),
    ("Java", [r"\bJava\b"]),
    ("JavaScript", [r"\bJavaScript\b", r"\bJava\s*Script\b"]),
    ("TypeScript", [r"\bTypeScript\b", r"\bType\s*Script\b"]),
    ("C", [
    r"(?<![A-Za-z0-9_+#])C(?!\s*Sharp)(?![A-Za-z0-9_+#])",
]),
    ("C++", [r"(?<![A-Za-z0-9_])C\+\+(?![A-Za-z0-9_])"]),
    ("C#", [
    r"(?<![A-Za-z0-9_])C#(?![A-Za-z0-9_])",
    r"\bC\s*Sharp\b",
]),
    ("Go", [r"\bGolang\b", r"\bGo\b"]),
    ("Rust", [r"\bRust\b"]),
    ("PHP", [r"\bPHP\b"]),
    ("Ruby", [r"\bRuby\b"]),
    ("Kotlin", [r"\bKotlin\b"]),
    ("Swift", [r"\bSwift\b"]),
    ("Scala", [r"\bScala\b"]),
    ("R", [r"(?<![A-Za-z0-9_])R(?![A-Za-z0-9_])"]),
    ("MATLAB", [r"\bMATLAB\b"]),
    ("HTML", [r"\bHTML\b"]),
    ("CSS", [r"\bCSS\b"]),
    ("React", [r"\bReact\b", r"\bReactJS\b", _ocr_tolerant_pattern("ReactJS")]),
    ("Angular", [r"\bAngular\b"]),
    ("Vue", [r"\bVue\b", r"\bVueJS\b", _ocr_tolerant_pattern("VueJS")]),
    ("Node.js", [r"\bNode\.js\b", r"\bNode\s*js\b", r"\bNodejs\b"]),
    ("Express", [r"\bExpress\b"]),
    ("Django", [r"\bDjango\b"]),
    ("Flask", [r"\bFlask\b"]),
    ("FastAPI", [r"\bFastAPI\b", r"\bFast\s*API\b"]),
    ("Spring Boot", [r"\bSpring\s*Boot\b", _ocr_tolerant_pattern("Spring Boot")]),
    ("ASP.NET", [r"\bASP\.NET\b", r"\bASP\s*NET\b", r"\bASPNET\b"]),
    ("MySQL", [r"\bMySQL\b", r"\bMy\s*SQL\b"]),
    ("PostgreSQL", [r"\bPostgreSQL\b", r"\bPostgre\s*SQL\b", r"\bPostgres\b"]),
    ("SQL Server", [r"\bSQL\s*Server\b", r"\bSQLServer\b"]),
    ("Oracle", [r"\bOracle\b"]),
    ("MongoDB", [r"\bMongoDB\b", r"\bMongo\s*DB\b"]),
    ("Redis", [r"\bRedis\b"]),
    ("SQLite", [r"\bSQLite\b", r"\bSqlite\b"]),
    ("Cassandra", [r"\bCassandra\b"]),
    ("Elasticsearch", [r"\bElasticsearch\b", r"\bElastic\s*Search\b"]),
    ("AWS", [r"\bAWS\b", r"\bAmazon\s+Web\s+Services\b"]),
    ("Azure", [r"\bAzure\b"]),
    ("Google Cloud", [r"\bGoogle\s*Cloud\b", r"\bGoogleCloud\b"]),
    ("GCP", [r"\bGCP\b"]),
    ("OCI", [r"\bOCI\b"]),
    ("OpenStack", [r"\bOpenStack\b"]),
    ("Docker", [r"\bDocker\b"]),
    ("Kubernetes", [r"\bKubernetes\b", r"\bk8s\b"]),
    ("Terraform", [r"\bTerraform\b"]),
    ("Ansible", [r"\bAnsible\b"]),
    ("Jenkins", [r"\bJenkins\b"]),
    ("GitHub Actions", [r"\bGitHub\s*Actions\b", r"\bGithub\s*Actions\b"]),
    ("GitLab CI", [r"\bGitLab\s*CI\b", r"\bGitlab\s*CI\b"]),
    ("TCP/IP", [r"\bTCP/IP\b", r"\bTCP\s*/\s*IP\b"]),
    ("BGP", [r"\bBGP\b"]),
    ("OSPF", [r"\bOSPF\b"]),
    ("MPLS", [r"\bMPLS\b"]),
    ("VPN", [r"\bVPN\b"]),
    ("LAN", [r"\bLAN\b"]),
    ("WAN", [r"\bWAN\b"]),
    ("Routing", [r"\bRouting\b"]),
    ("Switching", [r"\bSwitching\b"]),
    ("5G", [r"\b5G\b"]),
    ("4G LTE", [
    r"\b4G\s*LTE\b",
    r"\b4G\s*L\s*T\s*E\b",
    r"\bLTE\b",
]),
    ("VoLTE", [r"\bVoLTE\b"]),
    ("IMS", [r"\bIMS\b"]),
    ("GPON", [r"\bGPON\b"]),
    ("DWDM", [r"\bDWDM\b"]),
    ("SDH", [r"\bSDH\b"]),
    ("OTN", [r"\bOTN\b"]),
    ("MPLS-TP", [r"\bMPLS-TP\b", r"\bMPLS\s*[-/]\s*TP\b"]),
    ("Cisco", [r"\bCisco\b"]),
    ("Juniper", [r"\bJuniper\b"]),
    ("Nokia", [r"\bNokia\b"]),
    ("Huawei", [r"\bHuawei\b"]),
    ("Ericsson", [r"\bEricsson\b"]),
    ("Ciena", [r"\bCiena\b"]),
    ("Tejas", [r"\bTejas\b"]),
    ("Firewall", [r"\bFirewall\b"]),
    ("Fortinet", [r"\bFortinet\b"]),
    ("Palo Alto", [r"\bPalo\s*Alto\b", r"\bPaloAlto\b"]),
    ("CrowdStrike", [r"\bCrowdStrike\b"]),
    ("SIEM", [r"\bSIEM\b"]),
    ("SOC", [r"\bSOC\b"]),
    ("EDR", [r"\bEDR\b"]),
    ("XDR", [r"\bXDR\b"]),
    ("Machine Learning", [r"\bMachine\s*Learning\b", r"\bML\b"]),
    ("Deep Learning", [r"\bDeep\s*Learning\b"]),
    ("NLP", [r"\bNLP\b"]),
    ("LLM", [r"\bLLM\b"]),
    ("TensorFlow", [r"\bTensorFlow\b", r"\bTensor\s*Flow\b"]),
    ("PyTorch", [r"\bPyTorch\b", r"\bTorch\b"]),
    ("Scikit-learn", [r"\bScikit[-\s]*learn\b", r"\bsklearn\b"]),
    ("OpenAI API", [r"\bOpenAI\s*API\b", r"\bOpenAI\b"]),
    ("SAP", [r"\bSAP\b"]),
    ("Oracle ERP", [r"\bOracle\s*ERP\b", r"\bOracleERP\b"]),
    ("Salesforce", [
    r"\bSalesforce\b",
    r"\bSales\s*Force\b",
]),
    ("Workday", [r"\bWorkday\b"]),
    ("ServiceNow", [r"\bServiceNow\b", r"\bService\s*Now\b"]),
]


def _search_terms(text, skill_list):
    """
    Find skills preserving first occurrence order.
    OCR tolerant.
    Case insensitive.
    """

    if not text:
        return []

    matches = []

    for order, skill in enumerate(skill_list):

        patterns = [
            r"\b" + re.escape(skill) + r"\b",
            _ocr_tolerant_pattern(skill),
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                matches.append((match.start(), order, skill))
                break

    matches.sort(key=lambda item: (item[0], item[1]))

    result = []
    seen = set()

    for _, _, skill in matches:
        if skill not in seen:
            result.append(skill)
            seen.add(skill)

    return result


def _find_technical_skills(text):
    if not text:
        return []

    matches = []

    for order, (skill, patterns) in enumerate(TECHNICAL_SKILL_PATTERNS):
        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                matches.append((match.start(), order, skill))
                break

    known = {skill for skill, _ in TECHNICAL_SKILL_PATTERNS}
    for skill in TECHNICAL_SKILLS:
        if skill in known:
            continue
        pattern = r"\b" + re.escape(skill) + r"\b"
        for match in re.finditer(pattern, text, re.IGNORECASE):
            matches.append((match.start(), len(TECHNICAL_SKILL_PATTERNS), skill))
            break

    matches.sort(key=lambda item: (item[0], item[1]))

    ...
    normalized = []
    seen = set()

    for _, _, skill in matches:
        if skill not in seen:
            normalized.append(skill)
            seen.add(skill)

    # Remove generic skills when specific skills exist
   
    if "SQL Server" in normalized and "SQL" in normalized:
        normalized.remove("SQL")

    if "Oracle ERP" in normalized and "Oracle" in normalized:
        normalized.remove("Oracle")

    if "MPLS-TP" in normalized and "MPLS" in normalized:
        normalized.remove("MPLS")

    return normalized


def extract_skills(text):
    """
    Extract technical, functional and soft skills.
    """

    if not text:
        return {
            "technical_skills": [],
            "functional_skills": [],
            "soft_skills": [],
        }

    return {
        "technical_skills": _find_technical_skills(text),
        "functional_skills": _search_terms(text, FUNCTIONAL_SKILLS),
        "soft_skills": _search_terms(text, SOFT_SKILLS),
    }
