# JobFunClassifier

---

## Overview

The `JobFunClassifier` is a Python package designed for NLP-based job function classification. It helps categorize job positions based on their job descriptions. This tool is particularly valuable for roles that require cross-functional skills, providing insights into the specific job functions involved.

## Features

- **NLP Classification:** Utilizes Natural Language Processing techniques to classify job functions accurately.
- **26 Job Functions:** The model includes a comprehensive set of 26 job functions, ensuring a detailed and nuanced categorization.

<aside>
💡 ['Accounting', 'Finance', 'Administrative', 'IT and Development', 'Arts and Design', 'Customer service', 'Education', 'Corporate training', 'Engineering', 'Construction', 'Production', 'Healthcare Services', 'Pharmaceuticals', 'Hospitality', 'Travel', 'Human Resources', 'Law enforcement&Security', 'Legal', 'Logistics', 'Facilities', 'Marketing', 'Public Relations', 'Media and Communication', 'Real Estate', 'Sales', 'Retail']

</aside>

## **Why Use This Package?**

Understanding the job functions associated with a particular role is essential, especially in cross-functional environments. This classifier streamlines the process, making it easier to grasp the diverse responsibilities of a given job.

## **Prerequisites**

- Before using this package, ensure you have the following dependencies installed:

```bash
!pip install nltk
!pip install numpy
!pip install pandas
!pip install scipy
!pip install threadpoolctl
```

- Other required packages (specified in requirements.txt)

## Installation

To install the package, use the following pip command:

```bash
pip install JobFunClassifier
```

## Usage

---

- text : you can paste a description

```python
from JobFunClassifier.model import JobFunClassifier
model = JobFunClassifier()

text = """
Provides financial and investment planning and advice to deliver a solution in the best interests of the customer. Determines client needs and provides solutions though the sales of managed products and services (e.g. mutual funds, retirement savings plans, and similar products). Provides other solutions indirectly through referrals to business partners.

Takes a lead in proactively engaging with new and existing customers and prospects by providing needs-based assessments to grow loyalty and identify immediate/future opportunities.
Implements business development strategies to acquire new business (outbound calling campaigns and cultivating branch referrals).
Engages customers to grow BMO’s business by reaching out, generating appointments, and building new relationships within the community.
Identifies opportunities during customer conversations to generate referrals for personal and commercial banking products (e.g. personal banking, lending, and investments).
Supports the achievement of sales and performance targets.
Develops and implements a relationship management plan to meet the needs of client.
Responds to customer investment requests to fulfill investment product needs aligned with the customer’s goals and refers the customer to partners where appropriate.
Develops solutions and makes recommendations based on an understanding of the business strategy and stakeholder needs.
Breaks down strategic problems, and analyses data and information to provide insights and recommendations.
Executes work to deliver timely, accurate, and efficient service.
Introduces clients to investment strategies and works with clients to set goals and make real financial progress using appropriate guidance tools.
Probes to understand customer personal investment and banking needs and integrates marketing promotions and programs into customer conversations to provide strategic advice.
Looks for ways to contribute to the ongoing improvement of the overall business results and customer experience delivered.
Maintains current knowledge of personal investment products, practices, and trends and integrates into customer conversations.
May work at multiple branches and through various channels based on market needs to deliver the desired customer experience and achieve overall business objectives.
Builds effective relationships with internal/external stakeholders.
Protects the Bank's assets and complies with all regulatory, legal, and ethical requirements.
Focus may be on a business/group.
Thinks creatively and proposes new solutions.
Exercises judgment to identify, diagnose, and solve problems within given rules.
Works mostly independently.
Broader work or accountabilities may be assigned as needed.
Qualifications:

Typically between 3-5 years of relevant experience and post-secondary degree in related field of study or an equivalent combination of education and experience.
CFP designation preferred or one of the following:
Personal Financial Planner (PFP) designation,
Wealth Management Essentials (WME) + Financial Planning Supplement, Professional Financial Planning Course (PFPC),
Financial Planning I & II (FP I & II).
Canadian Securities Course - Licensed to sell mutual funds excluding QC or IQPF in Quebec.
Advanced working knowledge of financial industry.
Specialized knowledge from education and/or business experience.
Verbal & written communication skills - In-depth.
Collaboration & team skills - In-depth.
Analytical and problem solving skills - In-depth.
Influence skills - In-depth.
"""

output = model.predict(text, top=3)
```

```python
output
['Finance', 'Administrative', 'Sales']
```

## **References**

[Job descriptions Archives](https://resources.workable.com/job-descriptions/)

[A Pragmatic Approach to Build a Multi Label Text Classification with sklearn](https://medium.com/@johnidouglasmarangon/a-pragmatic-approach-to-build-a-multi-label-text-classification-with-sklearn-4e30c8126b57)