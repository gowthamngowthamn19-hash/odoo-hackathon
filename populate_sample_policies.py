import os
import base64
import sys
from datetime import date, timedelta

sys.path.append(r'C:\Program Files\Odoo 18.0.20260921\server')
import odoo
from odoo import api, SUPERUSER_ID

docs_dir = r'c:\Users\Admin\odoo-hackathon\sample_policy_documents'
os.makedirs(docs_dir, exist_ok=True)

POLICIES = [
    {
        'code': 'ENV-POL-001',
        'name': 'Climate Change & Net-Zero Carbon Strategy Policy',
        'category': 'environmental',
        'version': '2.1',
        'effective_date': '2026-01-15',
        'status': 'published',
        'filename': 'ENV-POL-001_Climate_Change_and_Net_Zero_Policy.md',
        'summary': 'Framework for greenhouse gas emissions inventory (Scope 1, 2, and 3), SBTi aligned decarbonization targets, renewable energy procurement, and annual carbon offsetting.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Climate Change & Net-Zero Carbon Strategy Policy
**Document Reference:** ENV-POL-001 | **Version:** 2.1 | **Effective Date:** January 15, 2026  
**ESG Pillar:** Environmental | **Applies To:** All Operations, Facilities & Business Units Worldwide

---

### 1. Executive Summary & Purpose
EcoSphere is committed to reaching Net-Zero Greenhouse Gas (GHG) emissions across our entire value chain by 2030, aligning with the 1.5°C Paris Agreement pathway and Science Based Targets initiative (SBTi). This policy defines our emissions reduction goals, energy management standards, and governance protocols to systematically eliminate carbon emissions.

### 2. Scope & Applicability
This policy applies to:
- All facilities, physical offices, data centers, and manufacturing sites operated by EcoSphere.
- Scope 1 (Direct emissions from combustion and company fleet).
- Scope 2 (Indirect emissions from purchased electricity, heating, and cooling).
- Scope 3 (Value chain emissions including business travel, logistics, supply chain procurement, and employee commuting).

### 3. Core Policy Commitments
1. **100% Renewable Energy by 2027**: All corporate offices and contracted data center operations must procure 100% certified renewable energy through direct Power Purchase Agreements (PPAs) or high-quality Energy Attribute Certificates (EACs/RECs).
2. **Facility Decarbonization**: Facility managers must transition HVAC systems to heat pumps, implement smart LED automated lighting, and enforce energy intensity benchmarks below 80 kWh/m² annually.
3. **Low-Emission Business Travel**:
   - Rail travel is mandatory for domestic and regional journeys under 400 km where feasible.
   - Air travel requires departmental ESG budget approval and must favor carriers utilizing Sustainable Aviation Fuel (SAF).
4. **Supply Chain Engagement**: By 2028, suppliers representing at least 75% of EcoSphere's Scope 3 emissions must have verified public SBTi decarbonization targets.
5. **High-Integrity Carbon Offsets**: Residual emissions may only be balanced using Gold Standard or Verra-certified permanent carbon removal projects (e.g., biochar, direct air capture, afforestation).

### 4. Responsibilities & Governance
- **Chief Sustainability Officer (CSO)**: Oversees policy execution, corporate carbon accounting, and annual disclosures (CDP, TCFD).
- **Facilities & Operations**: Ensures monthly utility monitoring, IoT sensor maintenance, and energy efficiency upgrades.
- **Finance & Procurement**: Enforces internal shadow carbon price of $65 per metric ton on capital expenditure proposals > $250,000.

### 5. Compliance & Audit
Compliance is audited biannually under ISO 14064 standards. Discrepancies or non-conformances must be logged in the EcoSphere Governance portal within 10 business days.
"""
    },
    {
        'code': 'ENV-POL-002',
        'name': 'Sustainable Procurement & Green Supply Chain Policy',
        'category': 'environmental',
        'version': '2.0',
        'effective_date': '2026-02-01',
        'status': 'published',
        'filename': 'ENV-POL-002_Sustainable_Procurement_Policy.md',
        'summary': 'Mandatory sustainability criteria, code of conduct, and life cycle assessments for all vendor contracts and hardware procurement.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Sustainable Procurement & Green Supply Chain Policy
**Document Reference:** ENV-POL-002 | **Version:** 2.0 | **Effective Date:** February 01, 2026  
**ESG Pillar:** Environmental | **Applies To:** Global Sourcing, Procurement, Vendors & Subcontractors

---

### 1. Purpose & Guiding Principles
EcoSphere integrates ESG considerations into every procurement decision to foster a responsible, low-impact, circular supply chain. We prioritize suppliers that exhibit verified environmental stewardship, transparent ethical conduct, and zero human rights abuses.

### 2. Mandatory Vendor Requirements
1. **EcoSphere Vendor Code of Conduct**: All suppliers with annual spend exceeding $50,000 must sign and comply with our Supplier ESG Code.
2. **Third-Party ESG Certification**: Suppliers must hold or actively work towards EcoVadis Bronze (minimum) or ISO 14001 certification within 12 months of contract engagement.
3. **Conflict-Free & Zero Deforestation**:
   - Mineral sourcing (tantalum, tin, tungsten, gold, cobalt) must strictly adhere to OECD Due Diligence Guidance.
   - Wood, paper, and bio-based products must be 100% FSC or PEFC certified.
4. **Circular Packaging Standards**:
   - 100% plastic-free or post-consumer recycled (PCR) content in primary packaging.
   - Single-use plastics are strictly prohibited in all incoming shipments.

### 3. Evaluation & Selection Criteria
Procurement tenders evaluate proposals using a weighted multi-factor scorecard:
- **Price & Commercials:** 40%
- **Technical Capabilities & Quality:** 35%
- **ESG & Decarbonization Roadmap:** 25%

### 4. Enforcement & Audit Rights
EcoSphere reserves the right to conduct unannounced on-site audits. Non-compliance results in a 60-day Corrective Action Plan (CAP). Failure to remediate terminates the vendor contract.
"""
    },
    {
        'code': 'ENV-POL-003',
        'name': 'Circular Economy, Waste Reduction & Hazardous Materials Policy',
        'category': 'environmental',
        'version': '1.5',
        'effective_date': '2026-03-01',
        'status': 'published',
        'filename': 'ENV-POL-003_Waste_Reduction_and_Circular_Economy_Policy.md',
        'summary': 'Zero waste-to-landfill standards, responsible electronic waste recycling, and strict chemical/hazardous waste containment.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Circular Economy, Waste Reduction & Hazardous Materials Policy
**Document Reference:** ENV-POL-003 | **Version:** 1.5 | **Effective Date:** March 01, 2026  
**ESG Pillar:** Environmental | **Applies To:** All Facilities, Laboratories & Warehouse Sites

---

### 1. Policy Objectives
EcoSphere adopts a closed-loop circular economy paradigm aimed at achieving certified Zero Waste to Landfill (ZWTL) (>90% diversion rate) across all global headquarters and operations by 2027.

### 2. Operational Waste Protocols
1. **Source Segregation**: Every workplace facility must provide segregated collection streams for organic composting, paper/cardboard, mixed recyclables, and residual waste.
2. **Elimination of Single-Use Items**: Single-use cutlery, beverage cups, and plastic bottles are prohibited in corporate kitchens, cafeterias, and catered events.
3. **Electronic Waste (E-Waste) Stewardship**:
   - All retired IT hardware (laptops, servers, peripherals) must be processed through R2 (Responsible Recycling) or e-Stewards certified partners.
   - Devices are audited for data sanitization (DoD 5220.22-M / NIST 800-88) followed by refurbishment, component reclamation, or materials recovery.
4. **Hazardous Materials & Chemicals**:
   - Storage of toxic, flammable, or corrosive substances must feature secondary containment systems capable of holding 110% of container volume.
   - Safety Data Sheets (SDS) must be digitized in the EcoSphere EHS portal and accessible to emergency personnel 24/7.
"""
    },
    {
        'code': 'ENV-POL-004',
        'name': 'Water Stewardship & Natural Resource Conservation Policy',
        'category': 'environmental',
        'version': '1.2',
        'effective_date': '2026-01-20',
        'status': 'published',
        'filename': 'ENV-POL-004_Water_Stewardship_Policy.md',
        'summary': 'Site-specific water footprint tracking, rainwater harvesting, greywater recycling, and local watershed replenishment.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Water Stewardship & Natural Resource Conservation Policy
**Document Reference:** ENV-POL-004 | **Version:** 1.2 | **Effective Date:** January 20, 2026  
**ESG Pillar:** Environmental | **Applies To:** All Facilities, Data Centers & Production Operations

---

### 1. Statement of Intent
Recognizing water as a vital shared resource, EcoSphere commits to responsible water stewardship across our operations, particularly in water-stressed geographic basins identified by the WRI Aqueduct Tool.

### 2. Action Standards
1. **Water Efficiency Targets**: All facilities must reduce municipal water consumption by 20% per capita by 2028 against a 2024 baseline.
2. **Infrastructure Requirements**:
   - Low-flow plumbing fixtures (aerated faucets, dual-flush systems).
   - Rainwater catchment systems for landscape irrigation and toilet flushing in company-owned buildings.
   - Closed-loop chilled water cooling systems in high-density compute rooms.
3. **Watershed Replenishment**: EcoSphere will invest in local watershed restoration projects to replenish 100% of water consumed in high-stress operational zones.
"""
    },
    {
        'code': 'SOC-POL-001',
        'name': 'Diversity, Equity, Inclusion & Anti-Discrimination Policy',
        'category': 'social',
        'version': '3.0',
        'effective_date': '2026-01-01',
        'status': 'published',
        'filename': 'SOC-POL-001_Diversity_Equity_Inclusion_Policy.md',
        'summary': 'Zero-tolerance anti-discrimination framework, gender pay parity guarantees, diverse recruitment slates, and inclusive workplace accommodations.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Diversity, Equity, Inclusion & Anti-Discrimination Policy
**Document Reference:** SOC-POL-001 | **Version:** 3.0 | **Effective Date:** January 01, 2026  
**ESG Pillar:** Social | **Applies To:** All Employees, Contractors, Job Applicants & Leadership

---

### 1. Purpose & Guiding Principles
EcoSphere believes diverse teams cultivate superior innovation, resilience, and business performance. We cultivate an inclusive workplace where all individuals are treated with dignity, fairness, and mutual respect, free from bias, prejudice, and unlawful discrimination.

### 2. Protected Characteristics & Zero Tolerance
Discrimination, harassment, microaggressions, or retaliation based on race, ethnicity, color, nationality, gender identity, sexual orientation, disability, age, religion, genetic background, or veteran status is strictly prohibited. Violations will result in disciplinary termination.

### 3. Operational DEI Commitments
1. **Diverse Recruitment Slates**: For all salaried leadership positions (Manager and above), hiring panels must interview candidate pools containing at least 50% underrepresented demographics.
2. **Annual Gender & Minority Pay Audits**:
   - An independent third-party audit of global compensation is conducted annually.
   - Any identified statistically unexplained pay gap greater than 1% across comparable roles must be remediated in the subsequent compensation cycle.
3. **Reasonable Accommodations**: EcoSphere guarantees full technical, physical, and scheduling accommodations for neurodivergent individuals and employees with disabilities.
4. **Employee Resource Groups (ERGs)**: Supported with executive sponsorship and dedicated annual operating budgets.
"""
    },
    {
        'code': 'SOC-POL-002',
        'name': 'Occupational Health, Safety & Employee Wellbeing Policy',
        'category': 'social',
        'version': '2.2',
        'effective_date': '2026-02-15',
        'status': 'published',
        'filename': 'SOC-POL-002_Health_Safety_and_Wellbeing_Policy.md',
        'summary': 'ISO 45001 workplace safety guidelines, mental health programs, hazard mitigation protocols, and ergonomic wellness standards.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Occupational Health, Safety & Employee Wellbeing Policy
**Document Reference:** SOC-POL-002 | **Version:** 2.2 | **Effective Date:** February 15, 2026  
**ESG Pillar:** Social | **Applies To:** Global Workforce, On-Site Visitors & Contractors

---

### 1. Core Commitment: "Zero Harm"
EcoSphere operates under the foundational belief that all workplace accidents, injuries, and occupational illnesses are preventable. We maintain an integrated EHS management system conforming to ISO 45001.

### 2. Health & Safety Protocols
1. **Hazard Identification & "Stop Work" Authority**: Every employee has the absolute right and obligation to halt any task, operation, or procedure immediately if they identify an imminent safety risk.
2. **Ergonomic Standards**: Workstation evaluations are provided for all remote, hybrid, and in-office staff, supported by an ergonomic stipend for certified home office setups.
3. **Comprehensive Mental Health Support**:
   - Free, 24/7 confidential Employee Assistance Program (EAP) counseling.
   - Mandatory mental health awareness training for all people managers.
4. **Incident & Near-Miss Reporting**: All occupational incidents and near-miss occurrences must be logged in the EcoSphere EHS module within 4 hours for swift root cause analysis.
"""
    },
    {
        'code': 'SOC-POL-003',
        'name': 'Human Rights & Fair Labor Standards Policy',
        'category': 'social',
        'version': '2.0',
        'effective_date': '2026-01-10',
        'status': 'published',
        'filename': 'SOC-POL-003_Human_Rights_and_Labor_Standards_Policy.md',
        'summary': 'Prohibition of child and forced labor, living wage requirements, humane working hours, and freedom of collective bargaining.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Human Rights & Fair Labor Standards Policy
**Document Reference:** SOC-POL-003 | **Version:** 2.0 | **Effective Date:** January 10, 2026  
**ESG Pillar:** Social | **Applies To:** Global Operations, Joint Ventures, Supply Chain

---

### 1. Universal Standards
EcoSphere upholds the United Nations Universal Declaration of Human Rights and the International Labour Organization (ILO) Fundamental Conventions. We reject any infringement on basic human dignity across our sphere of influence.

### 2. Fair Labor Rules
1. **Child Labor Prohibition**: No person under the age of 18 (or the local legal minimum working age, whichever is higher) may be employed in any capacity.
2. **Forced Labor & Modern Slavery**: All employment is voluntary. Debt bondage, retention of passports/identity papers, and recruitment fee deductions are strictly illegal.
3. **Living Wage Guarantee**: All direct employees are paid at or above certified regional Living Wage benchmarks (not merely statutory minimum wages).
4. **Working Hours & Rest Periods**: Standard work weeks must not exceed 48 hours, with at least one 24-hour continuous rest period every 7 consecutive days. Overtime must be voluntary and compensated at premium rates.
"""
    },
    {
        'code': 'SOC-POL-004',
        'name': 'Corporate Social Responsibility & Community Engagement Policy',
        'category': 'social',
        'version': '1.3',
        'effective_date': '2026-03-10',
        'status': 'published',
        'filename': 'SOC-POL-004_CSR_and_Community_Engagement_Policy.md',
        'summary': '24 hours annual paid volunteer time off (VTO), philanthropic donation matching, and grassroots STEM/sustainability partnerships.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Corporate Social Responsibility & Community Engagement Policy
**Document Reference:** SOC-POL-004 | **Version:** 1.3 | **Effective Date:** March 10, 2026  
**ESG Pillar:** Social | **Applies To:** All Full-Time and Part-Time Employees

---

### 1. Vision & Strategy
EcoSphere is dedicated to empowering local communities where our employees live and work. We combine financial contributions, employee expertise, and volunteerism to advance environmental regeneration and educational equity.

### 2. Employee Volunteering Program
- **Paid Volunteer Time Off (VTO)**: Every full-time employee receives up to 24 hours of fully paid leave annually to participate in approved community service, environmental cleanup, or non-profit projects.
- **EcoSphere Gamification Credits**: Completed volunteer hours logged in the EcoSphere platform earn employee XP toward annual recognition badges and tree-planting matches.

### 3. Charitable Matching Grants
EcoSphere matches dollar-for-dollar employee donations to certified 501(c)(3) or equivalent charitable non-profits up to $2,500 per employee per fiscal year.
"""
    },
    {
        'code': 'GOV-POL-001',
        'name': 'Anti-Bribery, Corruption & Anti-Money Laundering Policy',
        'category': 'governance',
        'version': '2.0',
        'effective_date': '2026-01-01',
        'status': 'published',
        'filename': 'GOV-POL-001_Anti_Bribery_and_Corruption_Policy.md',
        'summary': 'Strict anti-corruption compliance conforming to the US FCPA and UK Bribery Act. Strict $50 gift thresholds and third-party vetting.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Anti-Bribery, Corruption & Anti-Money Laundering Policy
**Document Reference:** GOV-POL-001 | **Version:** 2.0 | **Effective Date:** January 01, 2026  
**ESG Pillar:** Governance | **Applies To:** All Board Members, Officers, Employees, Intermediaries & Agents

---

### 1. Zero Tolerance Mandate
EcoSphere conducts business with the highest level of integrity. We maintain absolute zero tolerance for bribery, extortion, kickbacks, facilitation payments, and money laundering in any jurisdiction worldwide, regardless of local customs or competitive pressures.

### 2. Key Rules & Restrictions
1. **Prohibited Conduct**:
   - Offering, promising, giving, or authorizing any financial or other advantage to public officials or commercial partners to secure favorable business treatment.
   - Facilitation ("grease") payments to expedite routine administrative government actions are categorically forbidden.
2. **Gifts, Hospitality & Entertainment**:
   - Gifts exceeding $50 in value must receive prior written clearance from the Compliance Department.
   - Cash or cash equivalents (gift cards, vouchers) are strictly prohibited under all circumstances.
3. **Intermediaries & Third Parties**:
   - All sales agents, distributors, and lobbyists must undergo documented risk-based Anti-Corruption Due Diligence before onboarding.

### 3. Penalties & Legal Sanctions
Violations of this policy will result in immediate termination of employment, forfeiture of equity awards, and referral to criminal enforcement authorities.
"""
    },
    {
        'code': 'GOV-POL-002',
        'name': 'Whistleblower Protection & Non-Retaliation Policy',
        'category': 'governance',
        'version': '1.8',
        'effective_date': '2026-02-10',
        'status': 'published',
        'filename': 'GOV-POL-002_Whistleblower_Protection_Policy.md',
        'summary': '24/7 multi-lingual confidential ethics hotline, independent ombudsman investigations, and ironclad anti-retaliation legal protection.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Whistleblower Protection & Non-Retaliation Policy
**Document Reference:** GOV-POL-002 | **Version:** 1.8 | **Effective Date:** February 10, 2026  
**ESG Pillar:** Governance | **Applies To:** Current/Former Employees, Contractors, Vendors & Public

---

### 1. Purpose & Protection Guarantee
EcoSphere is committed to transparent, lawful operations. Anyone who suspects or discovers ethical misconduct, financial fraud, environmental violations, or safety hazards must feel empowered to speak up without fear of adverse consequences.

### 2. Reporting Channels
1. **Confidential Ethics Hotline**: Available 24/7 via toll-free phone and encrypted web portal, hosted by an independent third-party provider (anonymity fully preserved).
2. **Direct Reporting**: Reports may be made to the Chief Compliance Officer, Audit Committee Chair, or General Counsel.

### 3. Absolute Non-Retaliation Safeguards
- EcoSphere strictly forbids retaliation, demotion, termination, harassment, discrimination, or disadvantage against any individual who reports a concern in good faith.
- Any manager found engaging in retaliation will face immediate termination and potential civil liability.
- All investigations are conducted expeditiously by independent legal and forensic specialists.
"""
    },
    {
        'code': 'GOV-POL-003',
        'name': 'Data Privacy, AI Ethics & Cybersecurity Governance Policy',
        'category': 'governance',
        'version': '2.5',
        'effective_date': '2026-01-25',
        'status': 'published',
        'filename': 'GOV-POL-003_Data_Privacy_and_AI_Ethics_Policy.md',
        'summary': 'GDPR/CCPA compliance, end-to-end data encryption, algorithmic transparency, responsible generative AI boundaries, and incident response SLAs.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Data Privacy, AI Ethics & Cybersecurity Governance Policy
**Document Reference:** GOV-POL-003 | **Version:** 2.5 | **Effective Date:** January 25, 2026  
**ESG Pillar:** Governance | **Applies To:** IT Infrastructure, Software Development, Data Science & AI Systems

---

### 1. Strategic Principles
Digital trust is a cornerstone of corporate governance. EcoSphere implements Privacy-by-Design and ethical AI development across all algorithms, employee systems, and cloud platforms.

### 2. Data Privacy & Cybersecurity Protocols
1. **Compliance Standards**: Strict conformity with GDPR, CCPA/CPRA, and ISO/IEC 27001 / SOC 2 Type II information security baselines.
2. **Encryption & Access Control**:
   - All sensitive personal and proprietary corporate data must be encrypted using AES-256 at rest and TLS 1.3 in transit.
   - Mandatory Multi-Factor Authentication (MFA) and Zero-Trust network architecture.
3. **Data Subject Rights**: Automated self-service data access and deletion requests fulfilled within 14 calendar days.

### 3. Responsible AI & Copilot Framework
- **Algorithmic Fairness**: Automated AI models in EcoSphere (e.g., carbon prediction, HR talent matching) must undergo quarterly bias audits.
- **Data Confidentiality in LLMs**: Proprietary company source code, financial projections, and confidential customer metrics must never be uploaded to unvetted public generative AI tools.
"""
    },
    {
        'code': 'GOV-POL-004',
        'name': 'Executive ESG Accountability & Board Governance Policy',
        'category': 'governance',
        'version': '1.1',
        'effective_date': '2026-03-05',
        'status': 'published',
        'filename': 'GOV-POL-004_Executive_ESG_Accountability_Policy.md',
        'summary': 'Board independence quotas, linking 25% of executive bonuses to verified ESG benchmarks, clawback provisions, and annual ESG auditing.',
        'content': """# ECOSPHERE GLOBAL ENTERPRISE
## Policy Document: Executive ESG Accountability & Board Governance Policy
**Document Reference:** GOV-POL-004 | **Version:** 1.1 | **Effective Date:** March 05, 2026  
**ESG Pillar:** Governance | **Applies To:** Board of Directors, C-Suite Executives & Senior Leadership

---

### 1. Objective
To guarantee that corporate incentives align directly with long-term ecological preservation, social responsibility, and transparent shareholder value creation.

### 2. Board Composition & Oversight
1. **Independent Majority**: At least 60% of the Board of Directors must meet international independence standards.
2. **Board Diversity Target**: The Board must maintain at least 40% representation from historically underrepresented demographics.
3. **Dedicated ESG Committee**: The Board Sustainability & Risk Committee meets quarterly to audit carbon performance, regulatory compliance, and community impact.

### 3. Executive Compensation Linkage
- **25% ESG Performance Metric**: Annual executive variable compensation (bonuses and equity grants) is tied to measurable, third-party verified ESG outcomes:
  - 10%: Verified Scope 1/2 GHG reduction against annual milestone targets.
  - 8%: Employee DEI retention metrics and health/safety zero-harm score.
  - 7%: Governance audit score and supply chain compliance index.
- **Clawback Provisions**: Material misstatements of environmental data or compliance failures trigger mandatory compensation clawback over a rolling 36-month lookback period.
"""
    }
]

print(f"Creating {len(POLICIES)} sample policy documents in: {docs_dir}")

for p in POLICIES:
    filepath = os.path.join(docs_dir, p['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(p['content'])
    print(f"Written: {p['filename']}")

# Now insert / update in Odoo database
odoo.tools.config.parse_config(['-c', r'c:\Users\Admin\odoo-hackathon\odoo.conf', '-d', 'ecosphere'])
registry = odoo.registry('ecosphere')

with registry.cursor() as cr:
    env = api.Environment(cr, SUPERUSER_ID, {})
    Policy = env['eco.esg.policy']
    Attachment = env['ir.attachment']

    for p in POLICIES:
        filepath = os.path.join(docs_dir, p['filename'])
        with open(filepath, 'rb') as f:
            file_data = base64.b64encode(f.read())

        # Check if policy with this code or title exists
        existing = Policy.search(['|', ('policy_code', '=', p['code']), ('name', '=', p['name'])], limit=1)
        
        vals = {
            'name': p['name'],
            'policy_code': p['code'],
            'category': p['category'],
            'version': p['version'],
            'effective_date': p['effective_date'],
            'status': p['status'],
            'description': p['content'],
            'attachment_file': file_data,
            'attachment_filename': p['filename']
        }

        if existing:
            existing.write(vals)
            policy_rec = existing
            print(f"Updated policy: [{p['code']}] {p['name']}")
        else:
            policy_rec = Policy.create(vals)
            print(f"Created policy: [{p['code']}] {p['name']}")

        # Also create or update ir.attachment linked to the record so it shows in Chatter / Attachments
        att_existing = Attachment.search([
            ('res_model', '=', 'eco.esg.policy'),
            ('res_id', '=', policy_rec.id),
            ('name', '=', p['filename'])
        ], limit=1)

        if not att_existing:
            Attachment.create({
                'name': p['filename'],
                'datas': file_data,
                'res_model': 'eco.esg.policy',
                'res_id': policy_rec.id,
                'type': 'binary',
                'mimetype': 'text/markdown'
            })
            print(f"Attached document to chatter: {p['filename']}")

    cr.commit()
    print("All sample policy documents created and attached successfully!")
