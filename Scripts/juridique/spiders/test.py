# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector

class FirstSpider(scrapy.Spider): # créer une classe qui hérite scrapy.spiders.Spider
    # initialisation des champs
    name = "juridique" # obligatoire
    allowed_domains = ["wikipedia.org"] # optionnel
    start_urls = ["https://fr.wikipedia.org/wiki/Portail:Droit_fran%C3%A7ais/Arborescence#Liste_des_toutes_les_cat.C3.A9gories_li.C3.A9es"] # les premiers pages à télécharger


    # création de la fonction 'parse' (fonction callback dans la code source de Scrapy)
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'juritique-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)


        # extraction des données avec Scrapy shell
        # scrapy shell 'https://fr.wikipedia.org/wiki/Portail:Droit_fran%C3%A7ais/Arborescence#Liste_des_toutes_les_cat.C3.A9gories_li.C3.A9es'
        # Selectors : css ou xpath
        sel = Selector(response)
        yield {
            "title_extract_css" : sel.css('title::text').extract_first(),
            "title_extract_xpath" : sel.xpath('//title/text()').extract_first()
        }
        #print(sel.xpath('//div[@class="CategoryTreeSection"]/div[@class="CategoryTreeChildren" and preceding-sibling::div[1]/a[text()="Branche du droit"]]/div/div/a/text()').extract())
        branche_du_droit = sel.xpath('//div[@class="CategoryTreeSection"]/div[@class="CategoryTreeChildren" and preceding-sibling::div[1]/a[text()="Branche du droit"]]')
        #print(branche_du_droit)
        for section in branche_du_droit.xpath('.//div[@class="CategoryTreeChildren"]'):
            if section.xpath('./div'):
                print("-------pasée-------")
            else:
                print(section.xpath('../div[@class="CategoryTreeItem"]/a/text()').extract())




