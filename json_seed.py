import json
from st_app1.models import Company, Product

# season2, season3, season4, season5, season6
JSON_PATH = "json\\season6.json"


with open(JSON_PATH, encoding="utf-8") as jsonfile:
    reader = json.load(jsonfile)


# Getting episode from season
for key,val in reader.items():
    # episode_len = len(key);
    episode_len = len(reader.get(key))

    for item in range(0,episode_len):
        product_name = val[item].get('product')
        location = val[item].get('location')
        status = val[item].get('status')
        investors = val[item].get('investors')
        company_name = val[item].get('company')['title'].upper()
        if not company_name:
            continue
        if 'link' in val[item].get('company'):
            link = val[item].get('company')['link']
        else:
            link = ''
        company_dict = Company.objects.filter(company_name = company_name).values('id')
        if company_dict.exists():
            company_id = company_dict[0]['id']
        else:
            continue
            # company_id = ''
        Product.objects.create(product_name=product_name,location=location,
                                status = status, investors=investors,
                                company_name = Company.objects.get(id=company_id), link=link)
