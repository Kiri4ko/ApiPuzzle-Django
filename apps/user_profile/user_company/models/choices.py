#  Currency selection HEAD
class CurrSelect:
    USD = 'USD'
    EUR = 'EUR'
    CURRENCIES = [
        (USD, 'Dollars'),
        (EUR, 'Euro'),
    ]


#  Company choice PO
class CompanyChoice:
    STARTUP = 'Startup'
    SMALL = 'Small'
    MIDDLE = 'Middle'
    LARGE = 'Large'
    COMPANY = [
        (STARTUP, 'Startup'),
        (SMALL, 'Small (up to 50 people)'),
        (MIDDLE, 'Mid-size (up 200 people)'),
        (LARGE, 'Large (more than 200 people)'),
    ]


#  Choice industries PO and HEAD
class IndustryChoice:
    ECOMM = 'Ecommerce'
    AI = 'AI and Machine Learning'
    MARTECH = 'Martech (Marketing Tech)'
    LIVECHAT = 'Live Chat software'
    LOG = 'Logistics'
    DS = 'Data Science'
    HR = 'HR Software'
    WEBINAR = 'Webinar software'
    ELERN = 'eLearning'
    CYBER = 'Cybersecurity'
    AR = 'Augmented Reality'
    PM = 'Project Management software'
    FINTECH = 'Fintech'
    BLOCKCHAIN = 'Blockchain'
    MARKET = 'Marketplaces'
    SALE = 'Point of sale software'
    MOBILEDEV = 'Mobile Development'
    VOICEREC = 'Voice recognition'
    CRM = 'CRM software'
    GAMEDEV = 'Game Development'
    VIDEOREC = 'Video (Face) recognition'
    ERP = 'ERP software'

    INDUSTRIES = [
        (ECOMM, 'Ecommerce'), (AI, 'AI and Machine Learning'), (MARTECH, 'Martech (Marketing Tech)'),
        (LIVECHAT, 'Live Chat software'), (LOG, 'Logistics'), (DS, 'Data Science'), (HR, 'HR Software'),
        (WEBINAR, 'Webinar software'), (ELERN, 'eLearning'), (CYBER, 'Cybersecurity'), (AR, 'Augmented Reality'),
        (PM, 'Project Management software'), (FINTECH, 'Fintech'), (BLOCKCHAIN, 'Blockchain'), (MARKET, 'Marketplaces'),
        (SALE, 'Point of sale software'), (MOBILEDEV, 'Mobile Development'), (VOICEREC, 'Voice recognition'),
        (CRM, 'CRM software'), (GAMEDEV, 'Game Development'), (VIDEOREC, 'Video (Face) recognition'),
        (ERP, 'ERP software'),
    ]


#  Project start time
class ProjectStart:
    MONTH = 'This month'
    INMONTH = 'In a month'
    THREEMONTH = 'In three month time'
    YESTERDAY = 'Yesterday'
    TIMESTART = [
        (MONTH, 'This month'),
        (INMONTH, 'In a month'),
        (THREEMONTH, 'In three month time'),
        (YESTERDAY, 'Yesterday'),
    ]
