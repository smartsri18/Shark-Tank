from st_app1.models import Season, Episode, Company, Product

kwargs = {'season' : 1, 'episode' :1, 'gender':"Female", 'amount':"$50,000"}
d = Company.objects.get(**kwargs)
c = Product.objects.filter(investors="Barbara Corcoran").values('company_name','product_name','company_name_id')
print(c)
print(c[0]['product_name'])
print(d.id)
