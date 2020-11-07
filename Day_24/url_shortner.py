# Title  : Url shortner
# Author : Kiran Raj R.
# Date   : 07:11:2020

class URL_short:
    url_id = 0
    url_dict = {}
    def url_shortner(self,orginal_url):
        if orginal_url in self.url_dict:
            url = self.url_dict[orginal_url]
            return f"{orginal_url} already has a shorten url: my_url.com/{url}"

        else:
            url = str(hex(self.url_id))
            # print(url) 
            self.url_dict[orginal_url] = url
            self.url_id+=1
            return f"my_url.com/{url}"

    def return_site(self,short_url):
        url = short_url.split('/')[1]
        site = [key for key,value in self.url_dict.items() if value == url]
        if site == []:
            return f"{short_url} not found!!!"
        else:
            return site[0]

url_obj = URL_short()
site1 = url_obj.url_shortner('google.com')
site2 = url_obj.url_shortner('facebook.com')
site3 = url_obj.url_shortner('instagram.com')
site4 = url_obj.url_shortner('facebook.com')
# print(site1, site2, site3, site4)
# print(url_obj.url_dict)

print(url_obj.return_site('my_url.com/0x1'))
print(url_obj.return_site('my_url.com/0x21'))
print(site4)