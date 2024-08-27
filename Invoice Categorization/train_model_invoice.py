# train_model.py
import random
import spacy
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset

# Define the categories
category_names = {
    0: "Office Supplies",
    1: "Marketing and Advertising",
    2: "Utilities",
    3: "Software Licenses",
    4: "Professional Services",
    5: "Rent",
    6: "Travel and Accommodation",
    7: "Meals and Entertainment",
    8: "Maintenance and Repairs",
    9: "Transportation",
    10: "Insurance",
    11: "Salaries and Wages",
    12: "Training and Development",
    13: "Telecommunications",
    14: "Health and Safety",
    15: "Taxes and Compliance",
    16: "Inventory and Stock",
    17: "Loan Repayment",
    18: "Technology and IT Services",
    19: "Employee Benefits",
    20: "Sales",
    21: "Groceries"
}

sample_sentences = {
    "Office Supplies": [
        "We received an invoice from Staples for the bulk purchase of office supplies, including printer paper and pens.",
        "Amazon Business billed us for ergonomic chairs and standing desks for the office.",
        "The order from Office Depot included toner cartridges, sticky notes, and whiteboards for the new conference room.",
        "An invoice from Ryman listed various stationery items needed for the project.",
        "We were charged by OfficeMax for desk organizers, file folders, and ink for printers.",
        "Flipkart sent us a bill for the purchase of office essentials such as staplers, notepads, and mouse pads.",
        "The office was stocked with supplies from Viking Direct, as indicated by the recent invoice.",
        "Our latest supplies invoice from Wipro GE listed several items required for the expansion.",
        "Alibaba billed us for bulk orders of paper, envelopes, and pens for the new office in India.",
        "An invoice from Lyreco included office supplies like calculators, label makers, and storage boxes."
    ],
    "Marketing and Advertising": [
        "Google Ads invoiced us for the pay-per-click advertising campaign targeting new customers.",
        "The marketing team received a bill from Facebook for social media ad placements.",
        "We were charged by Ogilvy for creating a promotional video and online advertisements.",
        "An invoice from Times of India was received for the print advertisements in their weekend edition.",
        "LinkedIn Marketing Solutions billed us for the sponsored content promoting our latest service.",
        "We received an invoice from Twitter for the social media campaigns run during the product launch.",
        "The digital agency Wunderman Thompson sent us a bill for SEO optimization and content marketing.",
        "The marketing firm Leo Burnett invoiced us for billboard advertising across multiple locations.",
        "An invoice from India Today listed the costs for the magazine ads we placed this quarter.",
        "We were billed by Mailchimp for email marketing services and automated campaigns."
    ],
    "Utilities": [
        "The electricity bill from Con Edison was included in the utility expenses for the month.",
        "An invoice from British Gas covered the gas service charges for the office.",
        "The water utility bill from Thames Water was received this week.",
        "We were invoiced by Reliance Energy for the electricity consumed at our Mumbai office.",
        "The telecom company Jio billed us for the internet and phone services provided last month.",
        "An invoice from AT&T listed the monthly charges for the fiber-optic internet connection.",
        "The natural gas bill from SoCalGas was higher than expected due to the recent cold snap.",
        "Vodafone sent us an invoice for the mobile data plans used by our field agents.",
        "The power bill from Tata Power was paid for our regional office in Pune.",
        "We received a water bill from Aqua America for the consumption at our headquarters."
    ],
    "Software Licenses": [
        "The annual renewal invoice for our Microsoft Office 365 licenses arrived today.",
        "Adobe sent us a bill for the Creative Cloud licenses used by the design team.",
        "We were invoiced by Oracle for the database management software licenses.",
        "An invoice from Salesforce included the CRM licenses for the sales department.",
        "The billing for Autodesk AutoCAD software was received for the engineering team.",
        "Our annual subscription for Zoom video conferencing licenses was billed this month.",
        "SAP invoiced us for the ERP software licenses utilized across various departments.",
        "We received a bill from Atlassian for the Jira and Confluence software licenses.",
        "The invoice from Quick Heal included antivirus software licenses for all company computers.",
        "An invoice from Tally Solutions was received for the accounting software licenses used by the finance team."
    ],
    "Professional Services": [
        "The legal firm Clifford Chance sent an invoice for their consultation services during the merger.",
        "Deloitte billed us for auditing services and financial statement preparation.",
        "We received a bill from Ernst & Young for the tax advisory services provided last quarter.",
        "The consulting firm McKinsey & Company sent an invoice for their strategic advice on our expansion plans.",
        "An invoice from KPMG included fees for the risk assessment and compliance services.",
        "PricewaterhouseCoopers (PwC) billed us for the business process improvement consultancy.",
        "The recruitment agency Randstad sent us an invoice for their executive search services.",
        "We were invoiced by Accenture for the technology consulting services rendered last month.",
        "The law firm Baker McKenzie billed us for their intellectual property legal services.",
        "An invoice from Infosys Consulting listed the IT transformation services provided."
    ],
    "Rent": [
        "The monthly rent invoice for our New York office space was issued by WeWork.",
        "Regus sent an invoice for the rent of our coworking space in London.",
        "We received a rent bill for the leased warehouse from Godrej Properties.",
        "An invoice from JLL included the rent for our regional office in Dubai.",
        "The landlord billed us for the office space we occupy in the DLF Cyber City complex.",
        "The rent for our Tokyo office was billed by Mitsubishi Estate this quarter.",
        "We received an invoice for the rental of our distribution center in Bangalore from Prestige Group.",
        "Hiranandani sent us a rent bill for the office space in their business park.",
        "The landlord invoiced us for the rented retail space in a shopping mall in Mumbai.",
        "An invoice from Brookfield Properties listed the monthly rent for our Chicago headquarters."
    ],
    "Travel and Accommodation": [
        "We received a bill from Marriott for the hotel stay during the business trip to Paris.",
        "Delta Airlines sent an invoice for the flight tickets booked for the sales team.",
        "The car rental agency Zoomcars invoiced us for the vehicles rented during the conference in Berlin.",
        "MakeMyTrip billed us for the accommodation and travel bookings for the team’s visit to Delhi.",
        "An invoice from Airbnb listed the charges for the rented apartments during the project in Mumbai.",
        "The travel agency Thomas Cook sent a bill for the flight and hotel package to Singapore.",
        "We received an invoice from OYO Rooms for the hotel stay during the training program in Chennai.",
        "Goibibo billed us for the transportation services used during the client meetings in London.",
        "The bill from Taj Hotels covered the accommodation for the executive retreat in Goa.",
        "We received an invoice from Emirates for the business class flights to Dubai."
    ],
    "Meals and Entertainment": [
        "We were billed by Starbucks for catering coffee and snacks during the board meeting.",
        "The invoice from McDonald's covered the expenses for the team lunch after the seminar.",
        "We received a bill from Domino's Pizza for the dinner ordered during the late-night work session.",
        "The restaurant Olive Garden invoiced us for the client dinner last week.",
        "Zomato sent us an invoice for the meals delivered to the office during the workshop.",
        "An invoice from Le Meridien listed the expenses for the banquet organized for the annual party.",
        "We received a bill from Pizza Hut for the catering services provided during the training session.",
        "The entertainment invoice from PVR Cinemas covered the movie tickets for the team outing.",
        "We were billed by Barbeque Nation for the team lunch organized after the project completion.",
        "The Taj Mahal Hotel sent an invoice for the corporate dinner hosted in their banquet hall."
    ],
    "Maintenance and Repairs": [
        "The HVAC maintenance invoice from Carrier was received for the quarterly service.",
        "We were billed by Johnson Controls for the routine maintenance of the office security system.",
        "An invoice from Bosch covered the repairs of the office elevators.",
        "The contractor sent a bill for the repairs to the leaking roof at the main office.",
        "Our plumbing repair invoice from Roto-Rooter was higher than expected due to the emergency service call.",
        "We received a bill from Blue Star for the maintenance of the air conditioning units.",
        "The handyman service UrbanClap sent an invoice for the repairs done to the office furniture.",
        "An invoice from Siemens listed the maintenance work carried out on the electrical systems.",
        "We were billed by Godrej Appliances for the repair of the office refrigerators and microwaves.",
        "The pest control services from Rentokil were invoiced after their visit last month."
    ],
    "Transportation": [
        "The logistics company DHL invoiced us for the transportation of goods to our retail outlets.",
        "FedEx sent a bill for the express shipping of customer orders placed last week.",
        "We received an invoice from Blue Dart for the courier services used for document delivery.",
        "The transportation bill from Indian Railways covered the freight charges for bulk shipments.",
        "An invoice from Uber listed the ride services used by employees for client meetings.",
        "The trucking company XPO Logistics invoiced us for the long-haul transportation of products.",
        "We were billed by Maersk for the shipping of containers to international destinations.",
        "The invoice from UPS covered the parcel delivery services provided this month.",
        "We received a bill from DPD for the transportation of goods between our warehouses.",
        "An invoice from Vistara Airlines included the air freight charges for the shipment of high-value items."
    ],
    "Insurance": [
        "The insurance company AIG sent us an invoice for the renewal of our property insurance policy.",
        "We received a bill from Allianz for the annual premium on our business interruption insurance.",
        "LIC of India invoiced us for the group health insurance policy covering our employees.",
        "The auto insurance bill from State Farm was received for the company vehicles.",
        "We were billed by ICICI Lombard for the cyber insurance policy protecting our digital assets.",
        "An invoice from Prudential included the premium for the directors and officers (D&O) insurance.",
        "The life insurance policy premium was billed by Tata AIA Life Insurance.",
        "HDFC ERGO sent an invoice for the fire insurance coverage of our warehouse.",
        "We received a bill from Aviva for the employee life insurance plan.",
        "The invoice from New India Assurance listed the premium for our marine cargo insurance."
    ],
    "Salaries and Wages": [
        "The payroll service ADP sent us an invoice for processing the salaries of our employees.",
        "We received a bill from Paychex for managing the wages of our temporary staff.",
        "The HR firm PeopleStrong invoiced us for the salary disbursement services provided this month.",
        "An invoice from TCS covered the payroll outsourcing services for our international employees.",
        "We were billed by QuickBooks Payroll for handling the wages and tax filings for our team.",
        "The invoice from Mercer listed the costs for salary benchmarking and compensation analysis.",
        "We received a bill from Zenefits for the payroll management and benefits administration services.",
        "The staffing agency Adecco invoiced us for the wages paid to the contract workers.",
        "An invoice from Gusto was received for the payroll services provided for our U.S. employees.",
        "We were billed by ManpowerGroup for the salaries of temporary staff hired during peak season."
    ],
    "Training and Development": [
        "The training provider Udemy sent us an invoice for the online courses purchased for our employees.",
        "We received a bill from Coursera for the professional development programs enrolled by our team.",
        "The leadership workshop conducted by FranklinCovey was invoiced last month.",
        "An invoice from Skillsoft included the costs for the e-learning courses completed by our staff.",
        "The bill from Simplilearn covered the certification programs in project management and data analysis.",
        "We were invoiced by NIIT for the technical training provided to our IT team.",
        "An invoice from General Assembly listed the digital marketing bootcamp attended by our marketing department.",
        "The corporate training services from Dale Carnegie were billed after the completion of the sessions.",
        "We received a bill from Great Learning for the executive education programs undertaken by our managers.",
        "The invoice from LinkedIn Learning included the fees for various online training modules accessed by employees."
    ],
    "Telecommunications": [
        "The telecommunications company Verizon sent us an invoice for the office landline and internet services.",
        "We received a bill from AT&T for the mobile data plans used by our sales team.",
        "The broadband service provider Spectrum invoiced us for the high-speed internet connection.",
        "An invoice from Vodafone Idea covered the monthly charges for the corporate mobile connections.",
        "We were billed by Airtel for the leased line internet service provided at our headquarters.",
        "The telecom company Reliance Jio sent us a bill for the mobile services used by our field employees.",
        "The invoice from T-Mobile listed the costs for the mobile hotspot devices used during travel.",
        "We received a bill from BT Group for the telecommunications services provided to our UK office.",
        "An invoice from BSNL covered the broadband and landline services at our regional offices.",
        "The invoice from Tata Communications included the charges for the global conferencing services used."
    ],
    "Health and Safety": [
        "Apollo Pharmacy sent us an invoice for the bulk purchase of sanitizers and first aid kits.",
        "We received a bill from Fortis Healthcare for the annual health check-ups provided to employees.",
        "The chemist chain MedPlus invoiced us for the masks and gloves ordered for the office.",
        "An invoice from Dr. Reddy's Laboratories covered the cost of the flu vaccines administered to staff.",
        "The hospital bill from AIIMS included charges for the emergency medical treatment provided to an employee.",
        "We were billed by Cipla for the supply of essential medicines stocked in our first aid cabinets.",
        "An invoice from Max Healthcare listed the expenses for the occupational health and safety training provided.",
        "The pharmacy chain CVS sent us a bill for the over-the-counter medications purchased for the office.",
        "We received an invoice from Manipal Hospitals for the wellness program conducted last quarter.",
        "The chemist bill from Guardian Pharmacy included items like pain relievers, bandages, and antiseptics."
    ],
    "Taxes and Compliance": [
        "The tax advisory firm PwC sent an invoice for preparing and filing our corporate tax returns.",
        "We received a bill from KPMG for the VAT compliance services provided this quarter.",
        "An invoice from Deloitte included fees for the audit and compliance review of our financial statements.",
        "The tax consultancy EY billed us for the GST filing and advisory services.",
        "We were invoiced by Grant Thornton for assistance with regulatory filings and tax compliance.",
        "An invoice from BDO covered the costs for the transfer pricing analysis and documentation.",
        "The accounting firm RSM sent a bill for the preparation of the income tax returns for our business.",
        "We received an invoice from Mazars for the internal audit and compliance services rendered.",
        "The tax software provider Intuit QuickBooks billed us for the annual subscription used for tax filings.",
        "An invoice from Moore Stephens listed the fees for the compliance audit conducted last month."
    ],
    "Inventory and Stock": [
        "We received an invoice from Alibaba for the bulk order of inventory items to be stocked in our warehouses.",
        "Amazon Business billed us for the purchase of office supplies and inventory restocking.",
        "An invoice from Flipkart included the costs for the replenishment of retail stock.",
        "The supplier sent us a bill for the raw materials required for the production of our products.",
        "We were billed by Walmart for the bulk order of goods to be distributed across our stores.",
        "An invoice from Metro Cash and Carry covered the costs for the purchase of wholesale items.",
        "The vendor Snapdeal sent us an invoice for the inventory restocking of electronic goods.",
        "We received a bill from BigBasket for the bulk order of groceries and consumables for the pantry.",
        "The invoice from eBay included the charges for the inventory items sourced from international suppliers.",
        "We were billed by Costco for the large quantity of products purchased for our new retail outlet."
    ],
    "Loan Repayment": [
        "The bank ICICI sent us an invoice for the monthly repayment of the business loan.",
        "We received a bill from HDFC Bank for the EMI on our commercial property loan.",
        "The invoice from State Bank of India covered the interest and principal payments on the working capital loan.",
        "An invoice from Axis Bank listed the monthly installment for the machinery loan taken last year.",
        "We were billed by Kotak Mahindra Bank for the repayment of the equipment financing loan.",
        "The invoice from Citibank included the charges for the quarterly interest payment on our line of credit.",
        "We received a bill from Bank of America for the loan repayment on our corporate office mortgage.",
        "An invoice from Barclays Bank covered the scheduled payment on the business expansion loan.",
        "The bank HSBC sent us an invoice for the monthly repayment of the international trade loan.",
        "We were billed by Union Bank for the payment due on the vehicle loan taken for company cars."
    ],
    "Technology and IT Services": [
        "The IT services provider Infosys sent us an invoice for the software development and maintenance services provided.",
        "We received a bill from Wipro for the implementation of the new ERP system.",
        "The technology consulting firm TCS invoiced us for the cloud migration services completed last month.",
        "An invoice from HCL Technologies included the costs for the IT infrastructure management services.",
        "The billing from IBM covered the data analytics and business intelligence services rendered.",
        "We were billed by Capgemini for the cybersecurity solutions and risk assessment services.",
        "The invoice from Tech Mahindra listed the charges for the network installation and support services.",
        "We received a bill from Cognizant for the digital transformation consulting services provided.",
        "The IT firm Accenture sent us an invoice for the application development and maintenance services.",
        "An invoice from Oracle covered the cloud services and database management solutions utilized."
    ],
    "Employee Benefits": [
        "The benefits provider Aon sent us an invoice for the contributions to the employee health insurance plan.",
        "We received a bill from Mercer for the administration of the employee retirement savings plan.",
        "The invoice from MetLife included the premiums for the group life insurance coverage.",
        "An invoice from Prudential listed the costs for the disability insurance provided to employees.",
        "We were billed by Voya Financial for the retirement plan services offered to our staff.",
        "The benefits administrator Zenefits sent an invoice for the wellness programs and gym memberships provided.",
        "We received a bill from Cigna for the global health insurance plan covering our expatriate employees.",
        "The invoice from LIC of India included the charges for the employee pension plan contributions.",
        "An invoice from ICICI Prudential Life covered the employee term life insurance policy.",
        "We were billed by ManipalCigna Health Insurance for the group medical insurance plan renewal."
    ],
    "Sales": [
        "The invoice from Shopify covered the fees for the e-commerce platform services provided.",
        "We received a bill from Salesforce for the sales management software subscription.",
        "The company Xero sent us an invoice for the sales analytics tools used.",
        "An invoice from HubSpot listed the costs for the CRM system and lead generation services.",
        "We were billed by Zoho for the sales and marketing software used by our team.",
        "The billing from Freshsales covered the costs for the customer relationship management tools.",
        "We received a bill from QuickBooks for the sales tracking and reporting software.",
        "An invoice from Pipedrive included the subscription fees for the sales pipeline management.",
        "The sales tool from Monday.com invoiced us for the project management and sales tracking features.",
        "We were billed by Nimble for the social sales and CRM services utilized."
    ],
    "Groceries": [
        "The invoice from BigBasket covered the costs of bulk grocery supplies ordered for the office.",
        "We received a bill from Amazon Pantry for the restocking of essential groceries.",
        "The grocery store Walmart sent us an invoice for the bulk purchase of food items and beverages.",
        "An invoice from Metro Cash and Carry listed the expenses for stocking up on groceries for the staff kitchen.",
        "We were billed by Reliance Fresh for the delivery of fresh produce and other grocery items.",
        "The invoice from Spencers Retail covered the costs for purchasing groceries for the office pantry.",
        "We received a bill from Zepto for the organic groceries supplied to our office.",
        "An invoice from Grofers included the costs of various grocery items delivered to our workplace.",
        "The supermarket chain D-Mart sent us an invoice for the bulk purchase of snacks and beverages.",
        "We were billed by Blinkit for the groceries supplied to our staff canteen."
    ]
}



# Generate 1000 lines of training data
training_data = []

for _ in range(1000):
    category_index = random.randint(0, 21)
    category = category_names[category_index]
    description = random.choice(sample_sentences[category])
    training_data.append((description, category_index))

# Extract texts and labels for training
invoices = [description for description, label in training_data]
labels = [label for description, label in training_data]

# Preprocess the text using spaCy
def preprocess_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# Custom Dataset class
class InvoiceDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Train the model
def train_model(train_texts, train_labels, val_texts, val_labels, num_labels, model_dir='model'):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    train_encodings = tokenizer(train_texts, truncation=True, padding=True)
    val_encodings = tokenizer(val_texts, truncation=True, padding=True)

    # Create datasets
    train_dataset = InvoiceDataset(train_encodings, train_labels)
    val_dataset = InvoiceDataset(val_encodings, val_labels)

    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=num_labels)
    training_args = TrainingArguments(output_dir='./results', num_train_epochs=10, per_device_train_batch_size=16)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )

    trainer.train()

    # Save the model and tokenizer
    model.save_pretrained(model_dir)
    tokenizer.save_pretrained(model_dir)

# If this script is executed, start training
if __name__ == "__main__":
    # Train the model
    train_model(invoices, labels, invoices, labels, num_labels=len(category_names))
