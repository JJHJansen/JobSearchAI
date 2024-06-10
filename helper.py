import copy, math, datetime, pickle

entity_filter_dict = {
    "Investment firm": True,
    "AIFM": True,
    "UCITS management company": True,
    "EVC": False,
    "European Crowdfunding Service Provider": False,
    "Systematic internaliser": True,
    "Multilateral trading facility": True,
    "Regulated market": True,
    "Organised trading facility": False,
    "Approved reporting mechanism": False,
    "Approved publication arrangement": False,
    "ESF": False,
}

entity_filter = [key for key, value in entity_filter_dict.items() if value]

relevant_columns_rename_dict = {
    "ae_competentAuthority": "AUTHORITY",
    "collectorParent": "PARENT",
    "ae_officeType": "OFFICE_TYPE",
    "ae_isSme": "SME",
    "ae_headOfficeAddress": "HQ_LOC",
    "ae_entityTypeLabel": "ENTITY_TYPE",
    "ae_lei": "LEI",
    "ae_entityName": "NAME",
    "ae_homeMemberState": "HOME_COUNTRY",
    "ae_branchAddress": "BRANCH_LOC",
    "ae_comment": "COMMENT",
    "ae_entityTypeCode": "ENTITY_CODE",
    "ae_website": "WEBSITE",
    "ae_hostMemberState": "HOST_COUNTRY",
    "ae_status": "STATUS",
    "no_of_funds": "N_FUNDS",
}

def pkl_dump(data, filename, path):
    filename = path + filename
    file = open(filename, 'wb')
    pickle.dump(data, file)
    file.close()

def pkl_load(filename, path):
    filename = path + filename
    file = open(filename, 'rb')
    data = pickle.load(file)
    file.close()
    return data