#!/usr/bin/env python


# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones intact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript living_things.Habitat
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper:

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
    from dateutil.tz import tzoffset
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from general.models import GenreForURL
    from general.models import Article
    from general.models import Language

    # Processing model: living_things.models.Habitat

    from living_things.models import Habitat

    living_things_habitat_1 = Habitat()
    living_things_habitat_1.name = 'desert'
    living_things_habitat_1.slug = 'desert'
    living_things_habitat_1.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_1.climate = ''
    living_things_habitat_1.article =  importer.locate_object(Article, "id", Article, "id", 153, {'id': 153, 'excerpt': 'desert', 'kicker': 'desert', 'content': '<p>desert is a barren area of land where little precipitation occurs and consequently living conditions are hostile for plant and animal life. The lack of vegetation leaves deserts exposed to the wind, which can create sandstorms.</p>\r\n\r\n<p>DESERTS</p>\r\n\r\n<p>A desert is a barren area of land where little precipitation occurs and consequently living conditions are hostile for plant and animal life. The lack of vegetation leaves deserts exposed to the wind, which can create sandstorms. About one-third of the Earth&#39;s land surface is covered by deserts, which range in size from tiny patches of dried mud to huge, sandy expanses that cover hundreds of thousands of square miles.</p>\r\n\r\n<p>The world&#39;s largest desert, the Sahara, occupies an area of 3.5 million square miles, or about one-quarter of Africa. The largest in North America is the Sonoran Desert, which stretches across the U.S.-Mexico border and covers more than 120,000 square miles.</p>\r\n\r\n<p>Most deserts are located in subtropical and temperate regions, where the sun is strong and the air is dry. Precipitation in deserts averages less than 10 inches a year, although oases may receive considerably more.</p>\r\n\r\n<p>DESERT CLIMATE</p>\r\n\r\n<p>Deserts have a unique climate, one that is generally hot and dry. The high temperatures are a result of the intense solar radiation, while the low precipitation leads to a shortage of water. The air in deserts is also quite dry, due to the lack of moisture-carrying clouds and the strong winds that often blow through these regions.</p>\r\n\r\n<p>In the daytime, the hot air near the surface rises, creating a low-pressure area. This causes cooler air to flow in from higher elevations, creating the characteristic high daytime temperatures in deserts. At night, the process reverses, and the cool air near the surface falls, replacing the warm air that has risen.</p>\r\n\r\n<p>PLANTS AND ANIMALS</p>\r\n\r\n<p>Despite the harsh environment, plants and animals have adapted to life in the desert. One of the most characteristic features of deserts is the presence of cacti, which have evolved to store water in their thick, fleshy stems.</p>\r\n\r\n<p>Some deserts are also home to large mammals, such as lions and elephants, which have developed strategies for surviving in the arid conditions. Other animals that are common in deserts include scorpions, spiders, and snakes.</p>\r\n\r\n<p>People have also adapted to life in the desert. One common adaptation is the use of qanats, carefully engineered systems of underground channels that bring water to the surface. These systems have been used for centuries in arid regions such as the Middle East and North Africa.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:20:00+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:20:18.718421+00:00")} ) 
    living_things_habitat_1.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_1 = importer.save_or_locate(living_things_habitat_1)

    living_things_habitat_2 = Habitat()
    living_things_habitat_2.name = 'forest'
    living_things_habitat_2.slug = 'forest'
    living_things_habitat_2.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_2.climate = ''
    living_things_habitat_2.article =  importer.locate_object(Article, "id", Article, "id", 152, {'id': 152, 'excerpt': 'Forest', 'kicker': 'Forest', 'content': '<p>Forest</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:19:21+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:19:24.969694+00:00")} ) 
    living_things_habitat_2.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_2 = importer.save_or_locate(living_things_habitat_2)

    living_things_habitat_3 = Habitat()
    living_things_habitat_3.name = 'Sandy Beach'
    living_things_habitat_3.slug = 'sandy-beach'
    living_things_habitat_3.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_3.climate = ''
    living_things_habitat_3.article = None
    living_things_habitat_3.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_3 = importer.save_or_locate(living_things_habitat_3)

    living_things_habitat_4 = Habitat()
    living_things_habitat_4.name = 'deep-sea'
    living_things_habitat_4.slug = 'deep-sea'
    living_things_habitat_4.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_4.climate = ''
    living_things_habitat_4.article =  importer.locate_object(Article, "id", Article, "id", 138, {'id': 138, 'excerpt': 'Deep', 'kicker': 'Deep', 'content': '<p>Deep sea diving is a dangerous sport that involves descending to great depths beneath the surface of the water. The sport is popular among thrill seekers and those who are looking for an extreme challenge.</p>\r\n\r\n<p>Despite the dangers involved, deep sea diving is a popular sport that continues to grow in popularity. Many divers travel the world in search of new and exciting diving locations. Some of the most popular diving destinations include the Great Barrier Reef in Australia, the Red Sea in Egypt, and the wreck of the TITANIC in the North Atlantic Ocean.</p>\r\n\r\n<p>Deep sea diving can be a dangerous sport, and divers must take precautions to avoid harm. One of the most common dangers associated with deep sea diving is the risk of diving accidents. Divers can be injured or killed by diving accidents if they are not careful.</p>\r\n\r\n<p>Another danger associated with deep sea diving is the risk of decompression sickness. This occurs when a diver ascends to the surface too quickly and the nitrogen that is dissolved in the blood comes out of solution. This can cause the diver to experience a wide range of unpleasant symptoms, including pain, nausea, and vomiting. In extreme cases, decompression sickness can be fatal.</p>\r\n\r\n<p>Divers must also be aware of the risk of getting lost or stranded underwater. This can happen if the diver becomes separated from the rest of the diving party or if the dive site is not accurately marked.</p>\r\n\r\n<p>Despite the dangers involved, deep sea diving is a popular and exciting sport that can provide a thrill like no other. Those who are interested in learning more about deep sea diving should consider taking a diving course. There are many different courses available, and each one will teach you the basics of deep sea diving.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:11:11+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:11:24.660673+00:00")} ) 
    living_things_habitat_4.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_4 = importer.save_or_locate(living_things_habitat_4)

    living_things_habitat_5 = Habitat()
    living_things_habitat_5.name = 'savanna'
    living_things_habitat_5.slug = 'savanna'
    living_things_habitat_5.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_5.climate = ''
    living_things_habitat_5.article =  importer.locate_object(Article, "id", Article, "id", 156, {'id': 156, 'excerpt': 'savanna', 'kicker': 'savanna', 'content': '<p>A savanna is a grassland ecosystem characterized by the scattered trees and shrubs that are found in the tropics and subtropics. The word &quot;savanna&quot; is derived from the Native American word &quot;savane&quot;, meaning &quot;open grassland&quot;.</p>\r\n\r\n<p>Savannas are found in Africa, South America, India, and Australia. The largest savanna on Earth is the African savanna, which covers about 1.3 million square kilometers, or one-fifth of the African continent.</p>\r\n\r\n<p>A savanna is a transitional ecosystem between a forest and a desert. The trees and shrubs in a savanna provide food and shelter for the animals that live there. The animals that live in a savanna include lions, elephants, zebras, monkeys, and antelopes.</p>\r\n\r\n<p>The grass in a savanna is grazed by the animals that live there. The grass is also home to many insects, including grasshoppers and termites. The insects are food for the predators that live in a savanna.</p>\r\n\r\n<p>The savannas of Africa and South America are home to many different types of animals. The savannas of India and Australia are home to fewer animals, but the animals that live there are unique and interesting.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:21:38+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:21:48.711388+00:00")} ) 
    living_things_habitat_5.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_5 = importer.save_or_locate(living_things_habitat_5)

    living_things_habitat_6 = Habitat()
    living_things_habitat_6.name = 'sea'
    living_things_habitat_6.slug = 'sea'
    living_things_habitat_6.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_6.climate = ''
    living_things_habitat_6.article =  importer.locate_object(Article, "id", Article, "id", 141, {'id': 141, 'excerpt': 'sea', 'kicker': 'sea', 'content': '<p>sea</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:14:42+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:14:50.668081+00:00")} ) 
    living_things_habitat_6.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_6 = importer.save_or_locate(living_things_habitat_6)

    living_things_habitat_7 = Habitat()
    living_things_habitat_7.name = 'river'
    living_things_habitat_7.slug = 'river'
    living_things_habitat_7.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_7.climate = ''
    living_things_habitat_7.article =  importer.locate_object(Article, "id", Article, "id", 145, {'id': 145, 'excerpt': 'river', 'kicker': 'river', 'content': '<p>river</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:16:51+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:16:59.143928+00:00")} ) 
    living_things_habitat_7.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_7 = importer.save_or_locate(living_things_habitat_7)

    living_things_habitat_8 = Habitat()
    living_things_habitat_8.name = 'rocky-shore'
    living_things_habitat_8.slug = 'rocky-shore'
    living_things_habitat_8.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_8.climate = ''
    living_things_habitat_8.article =  importer.locate_object(Article, "id", Article, "id", 144, {'id': 144, 'excerpt': 'Rocky', 'kicker': 'Rocky', 'content': '<p>Rocky shorelines are a type of shoreline that is characterized by a rocky coastline. Rocky shorelines are common in areas where there is a lot of tectonic activity, such as along the edges of continents and around volcanoes. The rocks that make up a rocky shoreline can be a variety of different sizes and shapes, and they can be found at different depths below the surface of the water.</p>\r\n\r\n<p>One of the benefits of a rocky shoreline is that it provides a lot of protection from erosion. The rocks help to break up the force of the waves as they hit the coastline, which helps to reduce the amount of damage that is done to the shoreline. Rocky shorelines can also help to stabilize the beach and the sand dunes that are found near the coastline.</p>\r\n\r\n<p>Another benefit of a rocky shoreline is that it provides a habitat for a variety of different marine life. The rocks provide a place for fish and other marine life to hide and feed, and they also help to create a sheltered area where they can breed. Rocky shorelines can also be a place where marine life can find shelter from strong winds and bad weather.</p>\r\n\r\n<p>There are also a few disadvantages to having a rocky shoreline. One of the main disadvantages is that it can be difficult for people to access the shoreline. The rocks can be difficult to walk on and can be dangerous if you fall. Another disadvantage is that the rocks can be a hazard to boats and other watercraft. The rocks can damage boats and can cause accidents if people are not careful.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:16:04+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:16:19.638498+00:00")} ) 
    living_things_habitat_8.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_8 = importer.save_or_locate(living_things_habitat_8)

    living_things_habitat_9 = Habitat()
    living_things_habitat_9.name = 'lake'
    living_things_habitat_9.slug = 'lake'
    living_things_habitat_9.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_9.climate = ''
    living_things_habitat_9.article =  importer.locate_object(Article, "id", Article, "id", 150, {'id': 150, 'excerpt': 'lake', 'kicker': 'lake', 'content': '<p>lake</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:18:34+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:18:43.245358+00:00")} ) 
    living_things_habitat_9.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_9 = importer.save_or_locate(living_things_habitat_9)

    living_things_habitat_10 = Habitat()
    living_things_habitat_10.name = 'polar'
    living_things_habitat_10.slug = 'polar'
    living_things_habitat_10.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_10.climate = ''
    living_things_habitat_10.article =  importer.locate_object(Article, "id", Article, "id", 149, {'id': 149, 'excerpt': 'polar', 'kicker': 'polar', 'content': '<p>polar</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:17:59+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:18:02.961448+00:00")} ) 
    living_things_habitat_10.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_10 = importer.save_or_locate(living_things_habitat_10)

    living_things_habitat_11 = Habitat()
    living_things_habitat_11.name = 'tropical-rain-forest'
    living_things_habitat_11.slug = 'tropical-rain-forest'
    living_things_habitat_11.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_habitat_11.climate = ''
    living_things_habitat_11.article =  importer.locate_object(Article, "id", Article, "id", 140, {'id': 140, 'excerpt': 'tropical', 'kicker': 'tropical', 'content': '<p>The tropical rainforest is a beautiful and unique environment found near the Earth&#39;s equator. This lush jungle is home to a variety of plant and animal life, including many that are rare and endangered.</p>\r\n\r\n<p>The rainforest is named for its high rainfall, which can reach up to 200 inches (508 cm) per year. The warm, moist climate and jungle vegetation create the perfect conditions for trees to grow tall and for plants and animals to thrive.</p>\r\n\r\n<p>The trees in a tropical rainforest are typically taller and have bigger leaves than trees in other types of forests. This makes the rainforest canopy, the uppermost layer of trees, thick and shady. The dense jungle floor is full of ferns, orchids, and other epiphytes, plants that grow on top of other plants.</p>\r\n\r\n<p>The forest floor is also home to a variety of animals. Mammals include sloths, monkeys, and bats. Reptiles include snakes, lizards, and turtles. There are also many species of insects, including butterflies and beetles.</p>\r\n\r\n<p>The tropical rainforest is a vital part of the environment. It helps to regulate the Earth&#39;s climate and to produce oxygen. The rainforest also provides valuable resources such as lumber, fruit, and medicinal plants.</p>\r\n\r\n<p>Sadly, the tropical rainforest is under threat. Deforestation, the destruction of trees, is a major problem. Deforestation is often done to make way for farms or development, or to extract valuable resources like timber and minerals.</p>\r\n\r\n<p>If the tropical rainforest is destroyed, it can have serious consequences for the environment and for humans. The loss of the rainforest would remove a vital part of the Earth&#39;s ecosystem, and could lead to increased global temperatures and climate change. Deforestation could also reduce the amount of oxygen in the atmosphere and contribute to the loss of biodiversity.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:13:55+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:14:09.134160+00:00")} ) 
    living_things_habitat_11.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_11 = importer.save_or_locate(living_things_habitat_11)

    living_things_habitat_12 = Habitat()
    living_things_habitat_12.name = '砂漠'
    living_things_habitat_12.slug = 'desert-jp'
    living_things_habitat_12.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_12.climate = ''
    living_things_habitat_12.article =  importer.locate_object(Article, "id", Article, "id", 154, {'id': 154, 'excerpt': '砂漠', 'kicker': '砂漠', 'content': '<p>砂漠とは、雨がほとんど降らず、動植物の生息に適さない不毛の土地のことであり、植生がないために風にさらされ、砂嵐を引き起こす可能性がある。</p>\r\n\r\n<p>砂漠</p>\r\n\r\n<p>砂漠とは、雨がほとんど降らず、動植物の生息に適さない不毛の土地のことであり、植生がないために風にさらされ、砂嵐を引き起こす可能性がある。地球の陸地表面の約3分の1は砂漠で覆われており、その大きさは、乾燥した泥の小さなパッチから、数十万平方マイルを覆う巨大な砂地まで様々である。</p>\r\n\r\n<p>世界最大の砂漠であるサハラ砂漠の面積は350万平方マイルで、アフリカの約4分の1に相当する。北米最大の砂漠はソノラ砂漠で、米国とメキシコの国境にまたがり、面積は120,000平方マイル以上に及ぶ。</p>\r\n\r\n<p>ほとんどの砂漠は、太陽が強く、空気が乾燥している亜熱帯および温帯地域に位置している。砂漠の降水量は平均して年間10インチ未満であるが、オアシスはそれよりもかなり多くなる可能性がある。</p>\r\n\r\n<p>砂漠気候</p>\r\n\r\n<p>砂漠には独特の気候があり、一般的に暑くて乾燥した気候である。気温が高いのは強い太陽放射の結果であり、降水量が少ないと水が不足する。砂漠の空気もまた、水分を運ぶ雲がなく、これらの地域をしばしば吹く強い風のために、非常に乾燥している。</p>\r\n\r\n<p>日中には、地表近くの熱い空気が上昇して低圧領域を形成する。これにより、より低い空気がより高い高度から流入し、砂漠に特徴的な日中の高温を形成する。夜になると、このプロセスは逆になり、地表近くの冷たい空気が落下し、上昇した暖かい空気と置き換わる。</p>\r\n\r\n<p>植物と動物</p>\r\n\r\n<p>厳しい環境にもかかわらず、植物と動物は砂漠での生活に適応してきた。砂漠の最も特徴的な特徴の1つは、サボテンの存在である。サボテンは、厚くて多肉質の茎に水を貯蔵するように進化してきた。</p>\r\n\r\n<p>一部の砂漠には、ライオンやゾウなどの大型哺乳類が生息しており、乾燥した条件下で生き残るための戦略を開発してきた。砂漠によく見られるその他の動物には、サソリ、クモ、ヘビなどがある。</p>\r\n\r\n<p>人々は砂漠での生活にも適応してきた。一般的な適応の1つは、中東や北アフリカのような乾燥した地域で何世紀にもわたって使用されてきた、水を地表に運ぶ地下水路の慎重に設計されたシステムであるカナートの使用である。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:20:37+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:20:50.590199+00:00")} ) 
    living_things_habitat_12.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_12 = importer.save_or_locate(living_things_habitat_12)

    living_things_habitat_13 = Habitat()
    living_things_habitat_13.name = '森林'
    living_things_habitat_13.slug = 'forest-jp'
    living_things_habitat_13.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_13.climate = ''
    living_things_habitat_13.article =  importer.locate_object(Article, "id", Article, "id", 151, {'id': 151, 'excerpt': 'Forest', 'kicker': 'Forest', 'content': '<p>Forest</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:19:10+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:19:14.058837+00:00")} ) 
    living_things_habitat_13.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_13 = importer.save_or_locate(living_things_habitat_13)

    living_things_habitat_14 = Habitat()
    living_things_habitat_14.name = '砂浜'
    living_things_habitat_14.slug = 'sandy-beach-jp'
    living_things_habitat_14.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_14.climate = ''
    living_things_habitat_14.article = None
    living_things_habitat_14.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_14 = importer.save_or_locate(living_things_habitat_14)

    living_things_habitat_15 = Habitat()
    living_things_habitat_15.name = '深海'
    living_things_habitat_15.slug = 'deep-sea-jp'
    living_things_habitat_15.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_15.climate = ''
    living_things_habitat_15.article =  importer.locate_object(Article, "id", Article, "id", 137, {'id': 137, 'excerpt': '深海', 'kicker': '深海', 'content': '<p>深海ダイビングは、水面下の深いところまで潜る危険なスポーツで、スリルを求める人や極限のチャレンジを求める人に人気があります。</p>\r\n\r\n<p>危険が伴うにもかかわらず、深海ダイビングは人気のあるスポーツであり、人気は高まり続けています。多くのダイバーが、新しくて刺激的なダイビングスポットを求めて世界中を旅しています。最も人気のあるダイビングスポットには、オーストラリアのグレートバリアリーフ、エジプトの紅海、北大西洋のタイタニック号の残骸などがあります。</p>\r\n\r\n<p>深海ダイビングは危険なスポーツであるため、危険を回避するための予防措置を講じる必要があります。深海ダイビングに関連する最も一般的な危険の1つは、ダイビング事故のリスクです。ダイバーは注意しないと、ダイビング事故によって負傷したり死亡したりする可能性があります。</p>\r\n\r\n<p>深海潜水に関連するもう1つの危険は、減圧症のリスクです。これは、ダイバーがあまりにも速く海面に上昇し、血液に溶けている窒素が溶液から出てくる場合に発生します。これにより、ダイバーは痛み、吐き気、嘔吐などのさまざまな不快な症状を経験する可能性があります。極端な場合、減圧症は致命的になる可能性があります。</p>\r\n\r\n<p>ダイバーはまた、水中で迷子になったり、立ち往生したりするリスクを認識する必要があります。これは、ダイバーがダイビングパーティーの他のメンバーから離れてしまった場合や、ダイビングサイトが正確にマークされていない場合に発生する可能性があります。</p>\r\n\r\n<p>危険を伴うにもかかわらず、深海ダイビングは他に類を見ないスリルを提供できる人気のあるエキサイティングなスポーツです。深海ダイビングについてもっと学びたい人は、ダイビングコースを受けることを検討すべきです。利用可能な多くの異なるコースがあり、それぞれがあなたに深海ダイビングの基本を教えてくれます。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:10:33+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:10:56.981032+00:00")} ) 
    living_things_habitat_15.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_15 = importer.save_or_locate(living_things_habitat_15)

    living_things_habitat_16 = Habitat()
    living_things_habitat_16.name = 'サバンナ'
    living_things_habitat_16.slug = 'savanna-jp'
    living_things_habitat_16.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_16.climate = ''
    living_things_habitat_16.article =  importer.locate_object(Article, "id", Article, "id", 155, {'id': 155, 'excerpt': 'サバンナ', 'kicker': 'サバンナ', 'content': '<p>サバンナは、熱帯や亜熱帯に散在する樹木や潅木を特徴とする草原生態系であり、「サバンナ」という言葉は、「開けた草原」を意味するアメリカ先住民の言葉「savane」に由来する。</p>\r\n\r\n<p>サバンナは、アフリカ、南米、インド、オーストラリアに分布しており、地球上最大のサバンナはアフリカ大陸の5分の1にあたる約130万平方キロメートルの面積を占めるアフリカサバンナである。</p>\r\n\r\n<p>サバンナは、森林と砂漠の間の移行的な生態系である。サバンナの木や低木は、そこに住む動物に食料と住居を提供する。サバンナに住む動物には、ライオン、ゾウ、シマウマ、サル、アンテロープなどが含まれる。</p>\r\n\r\n<p>サバンナの草は、そこに住む動物によって放牧されています。また、草にはバッタやシロアリなどの多くの昆虫が生息しており、これらの昆虫はサバンナに住むTHE PREDATORSの餌となっています。</p>\r\n\r\n<p>アフリカや南米のサバンナにはさまざまな種類の動物が生息しています。インドやオーストラリアのサバンナに生息する動物は少ないですが、そこに生息する動物は独特で興味深いものです。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:21:12+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:21:25.112149+00:00")} ) 
    living_things_habitat_16.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_16 = importer.save_or_locate(living_things_habitat_16)

    living_things_habitat_17 = Habitat()
    living_things_habitat_17.name = '海'
    living_things_habitat_17.slug = 'sea-jp'
    living_things_habitat_17.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_17.climate = ''
    living_things_habitat_17.article =  importer.locate_object(Article, "id", Article, "id", 142, {'id': 142, 'excerpt': '海', 'kicker': '海', 'content': '<p>海</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:15:00+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:15:12.391446+00:00")} ) 
    living_things_habitat_17.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_17 = importer.save_or_locate(living_things_habitat_17)

    living_things_habitat_18 = Habitat()
    living_things_habitat_18.name = '川'
    living_things_habitat_18.slug = 'river-jp'
    living_things_habitat_18.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_18.climate = ''
    living_things_habitat_18.article =  importer.locate_object(Article, "id", Article, "id", 146, {'id': 146, 'excerpt': '川', 'kicker': '川', 'content': '<p>川</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:17:04+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:17:19.239611+00:00")} ) 
    living_things_habitat_18.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_18 = importer.save_or_locate(living_things_habitat_18)

    living_things_habitat_19 = Habitat()
    living_things_habitat_19.name = '岩場'
    living_things_habitat_19.slug = 'rocky-shore-jp'
    living_things_habitat_19.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_19.climate = ''
    living_things_habitat_19.article =  importer.locate_object(Article, "id", Article, "id", 143, {'id': 143, 'excerpt': '岩礁', 'kicker': '岩礁', 'content': '<p>岩礁海岸線は、岩の多い海岸線を特徴とする海岸線の一種です。岩礁海岸線は、大陸の端や火山の周辺など、地殻変動が多い地域でよく見られます。岩礁海岸線を構成する岩は、さまざまな大きさや形をしていて、水面下のさまざまな深さに見られます。</p>\r\n\r\n<p>岩礁海岸線の利点の1つは、浸食から多くの保護を提供することです。岩は、波が海岸線にぶつかるときに波の力を分散させるのに役立ち、海岸線に加えられる損傷の量を減らすのに役立ちます。岩礁海岸線は、海岸線近くにあるビーチや砂丘を安定させるのにも役立ちます。</p>\r\n\r\n<p>岩の多い海岸線のもう一つの利点は、さまざまな海洋生物の生息地を提供することである。岩は、魚や他の海洋生物が隠れて餌を食べる場所を提供するとともに、彼らが繁殖できる保護された地域を作るのに役立つ。岩の多い海岸線は、海洋生物が強風や悪天候から身を守る場所にもなり得る。</p>\r\n\r\n<p>また、海岸線が岩場であることには、いくつかの欠点もあります。主な欠点の1つは、人々が海岸線にアクセスするのが困難である可能性があることです。岩は歩くのが難しく、転倒した場合に危険になる可能性があります。もう1つの欠点は、岩が船や他の船舶に危険をもたらす可能性があることです。岩は船を損傷する可能性があり、注意しないと事故を引き起こす可能性があります。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:15:32+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:15:51.776901+00:00")} ) 
    living_things_habitat_19.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_19 = importer.save_or_locate(living_things_habitat_19)

    living_things_habitat_20 = Habitat()
    living_things_habitat_20.name = '湖'
    living_things_habitat_20.slug = 'lake-jp'
    living_things_habitat_20.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_20.climate = ''
    living_things_habitat_20.article =  importer.locate_object(Article, "id", Article, "id", 147, {'id': 147, 'excerpt': '湖', 'kicker': '湖', 'content': '<p>湖</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:17:37+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:18:28.628646+00:00")} ) 
    living_things_habitat_20.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_20 = importer.save_or_locate(living_things_habitat_20)

    living_things_habitat_21 = Habitat()
    living_things_habitat_21.name = '極地'
    living_things_habitat_21.slug = 'polar-jp'
    living_things_habitat_21.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_21.climate = ''
    living_things_habitat_21.article =  importer.locate_object(Article, "id", Article, "id", 148, {'id': 148, 'excerpt': 'polar', 'kicker': 'polar', 'content': '<p>polar</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:17:47+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:17:52.440903+00:00")} ) 
    living_things_habitat_21.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_21 = importer.save_or_locate(living_things_habitat_21)

    living_things_habitat_22 = Habitat()
    living_things_habitat_22.name = '熱帯雨林'
    living_things_habitat_22.slug = 'tropical-rain-forest-jp'
    living_things_habitat_22.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_habitat_22.climate = ''
    living_things_habitat_22.article =  importer.locate_object(Article, "id", Article, "id", 139, {'id': 139, 'excerpt': '熱帯雨林', 'kicker': '熱帯雨林', 'content': '<p>熱帯雨林は、地球の赤道付近に見られる美しくユニークな環境です。この青々としたジャングルには、希少で絶滅の危機に瀕している多くの生物を含む、さまざまな動植物が生息しています。</p>\r\n\r\n<p>この熱帯雨林の名前は、年間最大200インチ(508 cm)に達する降雨量にちなんで名付けられました。暖かく湿った気候とジャングルの植生は、樹木が高く成長し、動植物が繁栄するための完璧な条件を作り出しています。</p>\r\n\r\n<p>熱帯雨林の樹木は、一般的に他の種類の森林の樹木よりも背が高く、葉が大きい。そのため、樹木の最上層である熱帯雨林の林冠は厚くて日陰になっている。密生したジャングルの床には、シダやラン、その他の着生植物、他の植物の上に生育する植物でいっぱいである。</p>\r\n\r\n<p>林床には、ナマケモノ、サル、コウモリなどの哺乳類、ヘビ、トカゲ、カメなどの爬虫類、蝶やカブトムシなどの昆虫類など、さまざまな動物が生息しています。</p>\r\n\r\n<p>熱帯雨林は、地球の気候を調節し、酸素を生産するとともに、木材、果物、薬用植物などの貴重な資源を提供する重要な環境資源です。</p>\r\n\r\n<p>悲しいことに、熱帯雨林は脅威にさらされています。森林伐採、つまり樹木の破壊は大きな問題です。森林伐採は、農場や開発のために行われたり、木材や鉱物などの貴重な資源を採取するために行われることがよくあります。</p>\r\n\r\n<p>熱帯雨林が破壊されれば、地球の生態系の重要な部分が失われ、地球の気温の上昇や気候変動につながる可能性があり、また、森林破壊は大気中の酸素の量を減少させ、生物多様性の損失につながる可能性があり、環境や人間に深刻な影響を及ぼす可能性がある。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:13:37+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:13:49.839470+00:00")} ) 
    living_things_habitat_22.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 9, {'id': 9, 'name': 'living-things/habitats'} ) 
    living_things_habitat_22 = importer.save_or_locate(living_things_habitat_22)

    # Re-processing model: living_things.models.Habitat























