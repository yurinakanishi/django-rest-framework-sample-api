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
# manage.py dumpscript living_things.Species
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

    # Processing model: living_things.models.Species

    from living_things.models import Species

    living_things_species_1 = Species()
    living_things_species_1.name = 'mammal'
    living_things_species_1.slug = 'mammal'
    living_things_species_1.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_species_1.article =  importer.locate_object(Article, "id", Article, "id", 162, {'id': 162, 'excerpt': 'Mammal', 'kicker': 'Mammal', 'content': '<p>Mammal&#39;s, including humans, are all omnivores, which means that they are able to digest both animal and plant material. However, the proportion of animal to plant material in their diet can vary greatly from species to species.</p>\r\n\r\n<p>Herbivores, like deer and gazelles, consume mostly plant material, while carnivores, like lions and tigers, consume mostly meat. However, there are many species of mammals that fall somewhere in between, and consume both plant and animal material in varying proportions.</p>\r\n\r\n<p>This mixed diet is what allows mammals to be so adaptable and thrive in a wide variety of habitats. For example, lions can survive in the African savanna, where there is a lot of grass and other plant material, while also being able to survive in the rainforest, where there is more animal material available.</p>\r\n\r\n<p>Mammals typically eat a variety of different types of food, depending on what is available in their environment. They may eat fruits, vegetables, seeds, leaves, flowers, insects, and other small animals.</p>\r\n\r\n<p>Some mammals, like humans, are able to cook their food, which breaks down the tough plant cell walls and makes the nutrients in the food easier to digest. Cooking also makes some foods more palatable, which encourages animals to eat more of them.</p>\r\n\r\n<p>Other mammals, like chimpanzees, eat food raw. This is generally less efficient than cooking, because it can be more difficult to digest raw food, and it also means that the animals miss out on the nutritional benefits that cooking provides.</p>\r\n\r\n<p>However, there are some benefits to eating raw food. For example, raw food is often more satisfying than cooked food, and it can also be more environmentally sustainable, because cooking food requires extra resources like fuel.</p>\r\n\r\n<p>In general, mammals are able to digest a wide variety of food items, and they are able to adapt their diet to what is available in their environment. This allows them to be successful in a variety of different habitats.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:28:13+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:28:51.433574+00:00")} ) 
    living_things_species_1.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_1 = importer.save_or_locate(living_things_species_1)

    living_things_species_2 = Species()
    living_things_species_2.name = 'bird'
    living_things_species_2.slug = 'bird'
    living_things_species_2.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_species_2.article =  importer.locate_object(Article, "id", Article, "id", 169, {'id': 169, 'excerpt': 'bird', 'kicker': 'bird', 'content': '<p>bird</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:32:27+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:32:32.768880+00:00")} ) 
    living_things_species_2.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_2 = importer.save_or_locate(living_things_species_2)

    living_things_species_3 = Species()
    living_things_species_3.name = 'reptile'
    living_things_species_3.slug = 'reptile'
    living_things_species_3.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_species_3.article =  importer.locate_object(Article, "id", Article, "id", 160, {'id': 160, 'excerpt': 'Reptiles', 'kicker': 'Reptiles', 'content': '<p>Reptiles are ectothermic, meaning they rely on the environment to regulate their body temperature. For this reason, reptiles in the wild consume a varied diet to meet their nutritional needs. Captive reptiles, however, are typically fed a diet that is based on one or two types of food.</p>\r\n\r\n<p>Commercial reptile foods are available in a variety of forms, including as frozen, dried, and live food. The most common type of commercial reptile food is a frozen mix of different types of invertebrates, such as crickets, mealworms, and waxworms. Some frozen mixes also include small vertebrates, such as fish.</p>\r\n\r\n<p>Reptiles that are fed a diet based on live food typically consume more protein and fat than those that are fed a diet of frozen or dried food. Live food can also contain harmful bacteria and parasites that can cause health problems in reptiles.</p>\r\n\r\n<p>A diet that is based on a variety of different food sources is the healthiest for captive reptiles. A variety of food sources will provide the reptile with the vitamins and minerals it needs to stay healthy. A diet that is based on a single type of food, such as frozen invertebrates, can lead to nutritional deficiencies.</p>\r\n\r\n<p>Reptiles that are fed a diet of live food typically have a better-looking coat of scales and brighter colors than those that are fed a diet of frozen or dried food. Captive reptiles that are fed a diet of live food typically have a better appetite and are more active than those that are fed a diet of frozen or dried food.</p>\r\n\r\n<p>A diet that is based on a variety of different food sources is the healthiest for captive reptiles. A variety of food sources will provide the reptile with the vitamins and minerals it needs to stay healthy. A diet that is based on a single type of food, such as frozen invertebrates, can lead to nutritional deficiencies.</p>\r\n\r\n<p>Reptiles that are fed a diet of live food typically have a better-looking coat of scales and brighter colors than those that are fed a diet of frozen or dried food. Captive reptiles that are fed a diet of live food typically have a better appetite and are more active than those that are fed a diet of frozen or dried food.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:26:43+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:27:12.289834+00:00")} ) 
    living_things_species_3.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_3 = importer.save_or_locate(living_things_species_3)

    living_things_species_4 = Species()
    living_things_species_4.name = 'fish'
    living_things_species_4.slug = 'fish'
    living_things_species_4.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_species_4.article =  importer.locate_object(Article, "id", Article, "id", 165, {'id': 165, 'excerpt': 'Fish', 'kicker': 'Fish', 'content': '<p>Fish</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:30:19+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:30:50.524932+00:00")} ) 
    living_things_species_4.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_4 = importer.save_or_locate(living_things_species_4)

    living_things_species_5 = Species()
    living_things_species_5.name = 'insect'
    living_things_species_5.slug = 'insect'
    living_things_species_5.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_species_5.article =  importer.locate_object(Article, "id", Article, "id", 164, {'id': 164, 'excerpt': 'Insects', 'kicker': 'Insects', 'content': '<p>Insects are the most diverse group of animals on the planet, with over a million different species. They can be found in every environment, from the hottest deserts to the coldest mountains, and from the deepest oceans to the highest trees.</p>\r\n\r\n<p>Insects have six legs, and most have wings. They range in size from just a few millimetres to over a metre in length. They are eaters of all kinds of things, from plants to other animals, and some even eat decaying matter.</p>\r\n\r\n<p>Insects are an important part of the food chain. They are eaten by other animals, which in turn are eaten by even larger animals. Many insects are also important pollinators, helping to spread pollen from one plant to another.</p>\r\n\r\n<p>Insects are fascinating creatures, and there is much to learn about them. They are a vital part of the environment and the food chain, and play a role in pollination and the spread of pollen.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:29:42+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:29:55.742098+00:00")} ) 
    living_things_species_5.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_5 = importer.save_or_locate(living_things_species_5)

    living_things_species_6 = Species()
    living_things_species_6.name = 'amphibian'
    living_things_species_6.slug = 'amphibian'
    living_things_species_6.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_species_6.article =  importer.locate_object(Article, "id", Article, "id", 171, {'id': 171, 'excerpt': '両生類', 'kicker': '両生類', 'content': '<p>両生類は、カエル、ヒキガエル、イモリ、サンショウウオ、アシナシイモリを含む動物の一種である。両生類は350,000,000年以上前に魚から進化し、現在では南極を除くすべての大陸に生息している。彼らは外温性である。つまり、体内の温度を調節するために環境に依存している。両生類は滑らかで湿った皮膚を持っているので、脅威にさらされたときに水の中に滑り落ちやすい。彼らは通常、水中に卵を産み、そこで胚が孵化して成虫になる。</p>\r\n\r\n<p>両生類の綱は、カエルとヒキガエル、イモリとサンショウウオ、アシナシイモリの3つのグループに分けられる。カエルとヒキガエルは、両生類の中で最もよく知られ、広く分布しているグループである。彼らは、丈夫な体、水かきのある足、突き出た目を特徴とする。カエルとヒキガエルは、砂漠から熱帯雨林までのさまざまな生息地に生息しており、南極を除くすべての大陸で見られる。イモリとサンショウウオの幼生はオタマジャクシとして知られている。オタマジャクシは長い尾と扁平な体を持ち、さまざまな水生生息地で見られる。アシナシイモリは、両生類の中で最も理解されていないグループである。彼らは、湿った土壌や葉のごみの中に住む虫のような生物である。</p>\r\n\r\n<p>両生類は外温性である。つまり、体内の温度を調節するために環境に依存している。この特性により、彼らは高温の砂漠から冷たい渓流まで、さまざまな生息地に住むことができる。両生類は滑らかで湿った皮膚を持っているので、脅威にさらされたときに水の中に滑り落ちやすい。彼らは通常、水の中に卵を産み、そこで胚が孵化して成虫になる。</p>\r\n\r\n<p>両生類は食物網の重要な一部であり、魚類、鳥類、ヘビ類、哺乳類を含むさまざまな捕食者の餌であり、有機物の分解にも重要な役割を果たしている。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:33:12+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:33:21.747465+00:00")} ) 
    living_things_species_6.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_6 = importer.save_or_locate(living_things_species_6)

    living_things_species_7 = Species()
    living_things_species_7.name = 'crustacean'
    living_things_species_7.slug = 'crustacean'
    living_things_species_7.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_species_7.article =  importer.locate_object(Article, "id", Article, "id", 167, {'id': 167, 'excerpt': 'Crustaceans', 'kicker': 'Crustaceans', 'content': '<p>Crustaceans are a type of marine animal that has a hard outer skeleton and jointed legs. They can be found in both salt and fresh water, and include creatures like crabs, lobsters, and shrimp.</p>\r\n\r\n<p>Crustaceans are an important part of the ocean food chain. They are a source of food for larger animals, and also play a role in keeping the ocean&#39;s ecosystem in balance.</p>\r\n\r\n<p>Crabs are the most common type of crustacean. They can be found in all parts of the world, and come in a wide variety of shapes and sizes. Crabs live in both salt and fresh water, and can be found on both the ocean floor and in rivers and streams.</p>\r\n\r\n<p>Lobsters are another type of crustacean that is found in coastal waters all over the world. Lobsters are a popular food item, and can be found in both fresh and salt water.</p>\r\n\r\n<p>Shrimp are the smallest type of crustacean. They are found in both salt and fresh water, and are a popular food item.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:31:33+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:31:51.816094+00:00")} ) 
    living_things_species_7.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_7 = importer.save_or_locate(living_things_species_7)

    living_things_species_8 = Species()
    living_things_species_8.name = 'mollusk'
    living_things_species_8.slug = 'mollusk'
    living_things_species_8.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_species_8.article =  importer.locate_object(Article, "id", Article, "id", 158, {'id': 158, 'excerpt': 'Mollusca', 'kicker': 'Mollusca', 'content': '<p>Mollusca is a large and diverse phylum of invertebrate animals. Around 85,000 species of mollusks are described, accounting for about one-third of all described invertebrate species. Mollusks include snails, clams, octopuses, and squids.</p>\r\n\r\n<p>The mollusk phylum is divided into 9 classes.</p>\r\n\r\n<p>The gastropods are the largest class of mollusks and include snails and slugs. Gastropods have a single, spirally coiled shell.</p>\r\n\r\n<p>The cephalopods are the second largest class of mollusks and include octopuses and squids. Cephalopods are characterized by their eight arms and two tentacles.</p>\r\n\r\n<p>The bivalves are a class of mollusks that include clams and mussels. Bivalves are characterized by their two shells that are hinged together.</p>\r\n\r\n<p>The scaphopods are a small class of mollusks that include the tusk shells. Scaphopods are characterized by their elongated, tubular shells.</p>\r\n\r\n<p>The monoplacophorans are a small class of mollusks that are the most primitive group of mollusks. Monoplacophorans are characterized by their single, curved shell.</p>\r\n\r\n<p>The polyplacophorans are a small class of mollusks that include the chitons. Polyplacophorans are characterized by their eight, overlapping plates that cover their body.</p>\r\n\r\n<p>The aplacophorans are a small class of mollusks that are characterized by their lack of a shell. Aplacophorans include the worm-like mollusks.</p>\r\n\r\n<p>The ctenophores are a small class of animals that are related to the jellyfish. Ctenophores are characterized by their eight, comb-like tentacles.</p>\r\n\r\n<p>The mollusks are a very diverse and widespread group of animals. They can be found in both marine and freshwater habitats. Mollusks are an important part of the food web and play a role in the ecology of their ecosystems.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:25:49+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:25:59.046144+00:00")} ) 
    living_things_species_8.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_8 = importer.save_or_locate(living_things_species_8)

    living_things_species_9 = Species()
    living_things_species_9.name = '哺乳類'
    living_things_species_9.slug = 'mammal-jp'
    living_things_species_9.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_species_9.article =  importer.locate_object(Article, "id", Article, "id", 161, {'id': 161, 'excerpt': '哺乳類', 'kicker': '哺乳類', 'content': '<p>ヒトを含む哺乳類はすべて雑食性であり、動物と植物の両方の物質を消化することができる。しかし、食物中の動物と植物の割合は種によって大きく異なる。</p>\r\n\r\n<p>シカやガゼルのような草食者は主に植物を消費し、ライオンやトラのような肉食動物は主に肉を消費する。しかし、その中間に位置し、植物と動物の両方の物質をさまざまな割合で消費する哺乳類の種も多い。</p>\r\n\r\n<p>この混合食は、哺乳類が多様な生息地で適応し、繁栄することを可能にするものである。例えば、ライオンは、草やその他の植物が豊富なアフリカのサバンナで生き残ることができ、一方で、より多くの動物物質が利用可能な熱帯雨林でも生き残ることができる。</p>\r\n\r\n<p>哺乳類は通常、環境中で利用可能なものに応じて、様々な異なる種類の食物を摂取する。果物、野菜、種子、葉、花、昆虫、その他の小動物を食べることがある。</p>\r\n\r\n<p>ヒトのような一部の哺乳類は、食物を調理することができ、それによって丈夫な植物の細胞壁が破壊され、食物中の栄養素が消化しやすくなる。また、調理によって一部の食物の味が良くなり、動物がより多くの食物を摂取するようになるという効果もある。</p>\r\n\r\n<p>チンパンジーのような他の哺乳類は食物を生で食べるが、これは一般に調理よりも効率が悪い。なぜなら、生の食物を消化することはより困難であり、また、動物は調理がもたらす栄養上の利益を逃してしまうからである。</p>\r\n\r\n<p>しかし、生の食品を食べることにはいくつかの利点があります。例えば、生の食品は調理された食品よりも満足度が高いことが多く、また、調理された食品は燃料のような余分な資源を必要とするため、環境的により持続可能である可能性もあります。</p>\r\n\r\n<p>一般に、哺乳類は多種多様な食物を消化することができ、環境中で利用可能なものに食物を適応させることができるので、さまざまな生息場所で成功することができる。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:27:41+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:28:10.107953+00:00")} ) 
    living_things_species_9.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_9 = importer.save_or_locate(living_things_species_9)

    living_things_species_10 = Species()
    living_things_species_10.name = '鳥類'
    living_things_species_10.slug = 'bird-jp'
    living_things_species_10.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_species_10.article =  importer.locate_object(Article, "id", Article, "id", 168, {'id': 168, 'excerpt': '鳥', 'kicker': '鳥', 'content': '<p>鳥</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:32:19+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:32:22.655564+00:00")} ) 
    living_things_species_10.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_10 = importer.save_or_locate(living_things_species_10)

    living_things_species_11 = Species()
    living_things_species_11.name = '爬虫類'
    living_things_species_11.slug = 'reptile-jp'
    living_things_species_11.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_species_11.article =  importer.locate_object(Article, "id", Article, "id", 159, {'id': 159, 'excerpt': '爬虫類', 'kicker': '爬虫類', 'content': '<p>爬虫類は外温性であり、体温を調節するために環境に依存していることを意味する。このため、野生の爬虫類は栄養上の必要性を満たすために様々な食事を摂取する。しかし、捕獲された爬虫類は通常、1種類または2種類の食物に基づく食事を与えられる。</p>\r\n\r\n<p>市販の爬虫類食品は、冷凍、乾燥、および生きた食品を含む様々な形態で入手可能である。市販の爬虫類食品の最も一般的なタイプは、コオロギ、ミールワーム、およびワムシなどの異なるタイプの無脊椎動物の冷凍混合物である。冷凍混合物の中には、魚などの小さな脊椎動物も含まれる。</p>\r\n\r\n<p>生きた食物をベースにした食事を与えられた爬虫類は、一般的に、冷凍または乾燥した食物を与えられた爬虫類よりも多くのタンパク質および脂肪を消費する。生きた食物には、爬虫類の健康問題を引き起こす可能性のある有害な細菌や寄生虫が含まれていることもあります。</p>\r\n\r\n<p>様々な異なる食物源に基づく食事は、捕獲された爬虫類にとって最も健康的である。様々な食物源が、健康を維持するために必要なビタミンとミネラルを爬虫類に提供する。冷凍無脊椎動物のような単一の種類の食物に基づく食事は、栄養不足につながる可能性がある。</p>\r\n\r\n<p>生きた食物を餌として与えられた爬虫類は、典型的には、冷凍または乾燥した食物を餌として与えられた爬虫類よりも、見た目の良いうろこの皮と明るい色をしている。生きた食物を餌として与えられた捕獲爬虫類は、典型的には、冷凍または乾燥した食物を餌として与えられた爬虫類よりも食欲があり、活発である。</p>\r\n\r\n<p>様々な異なる食物源に基づく食事は、捕獲された爬虫類にとって最も健康的である。様々な食物源が、健康を維持するために必要なビタミンとミネラルを爬虫類に提供する。冷凍無脊椎動物のような単一の種類の食物に基づく食事は、栄養不足につながる可能性がある。</p>\r\n\r\n<p>生きた食物を餌として与えられた爬虫類は、典型的には、冷凍または乾燥した食物を餌として与えられた爬虫類よりも、見た目の良いうろこの皮と明るい色をしている。生きた食物を餌として与えられた捕獲爬虫類は、典型的には、冷凍または乾燥した食物を餌として与えられた爬虫類よりも食欲があり、活発である。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:26:25+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:26:36.663209+00:00")} ) 
    living_things_species_11.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_11 = importer.save_or_locate(living_things_species_11)

    living_things_species_12 = Species()
    living_things_species_12.name = '魚類'
    living_things_species_12.slug = 'fish-jp'
    living_things_species_12.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_species_12.article = None
    living_things_species_12.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_12 = importer.save_or_locate(living_things_species_12)

    living_things_species_13 = Species()
    living_things_species_13.name = '昆虫'
    living_things_species_13.slug = 'insect-jp'
    living_things_species_13.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_species_13.article =  importer.locate_object(Article, "id", Article, "id", 163, {'id': 163, 'excerpt': '昆虫', 'kicker': '昆虫', 'content': '<p>昆虫は地球上で最も多様な動物のグループであり、100万種以上の異なる種がいる。それらは、最も暑い砂漠から最も寒い山まで、そして最も深い海から最も高い木まで、あらゆる環境で見られる。</p>\r\n\r\n<p>昆虫は6本の足を持ち、ほとんどは翼を持っている。それらの大きさはわずか数ミリメートルから長さ1メートル以上まで様々である。彼らは植物から他の動物まであらゆる種類のものを食べ、中には腐敗した物質を食べるものさえある。</p>\r\n\r\n<p>昆虫は食物連鎖の重要な部分である。昆虫は他の動物に食べられ、次に他の動物はさらに大きな動物に食べられる。多くの昆虫は重要な花粉媒介者でもあり、ある植物から別の植物への花粉の拡散を助ける。</p>\r\n\r\n<p>昆虫は魅力的な生物であり、学ぶべきことがたくさんあります。昆虫は環境や食物連鎖の重要な一部であり、受粉や花粉の拡散に重要な役割を果たしています。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:29:22+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:29:34.654437+00:00")} ) 
    living_things_species_13.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_13 = importer.save_or_locate(living_things_species_13)

    living_things_species_14 = Species()
    living_things_species_14.name = '両生類'
    living_things_species_14.slug = 'amphibian-jp'
    living_things_species_14.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_species_14.article =  importer.locate_object(Article, "id", Article, "id", 170, {'id': 170, 'excerpt': '両生類', 'kicker': '両生類', 'content': '<p>両生類は、カエル、ヒキガエル、イモリ、サンショウウオ、アシナシイモリを含む動物の一種である。両生類は350,000,000年以上前に魚から進化し、現在では南極を除くすべての大陸に生息している。彼らは外温性である。つまり、体内の温度を調節するために環境に依存している。両生類は滑らかで湿った皮膚を持っているので、脅威にさらされたときに水の中に滑り落ちやすい。彼らは通常、水中に卵を産み、そこで胚が孵化して成虫になる。</p>\r\n\r\n<p>両生類の綱は、カエルとヒキガエル、イモリとサンショウウオ、アシナシイモリの3つのグループに分けられる。カエルとヒキガエルは、両生類の中で最もよく知られ、広く分布しているグループである。彼らは、丈夫な体、水かきのある足、突き出た目を特徴とする。カエルとヒキガエルは、砂漠から熱帯雨林までのさまざまな生息地に生息しており、南極を除くすべての大陸で見られる。イモリとサンショウウオの幼生はオタマジャクシとして知られている。オタマジャクシは長い尾と扁平な体を持ち、さまざまな水生生息地で見られる。アシナシイモリは、両生類の中で最も理解されていないグループである。彼らは、湿った土壌や葉のごみの中に住む虫のような生物である。</p>\r\n\r\n<p>両生類は外温性である。つまり、体内の温度を調節するために環境に依存している。この特性により、彼らは高温の砂漠から冷たい渓流まで、さまざまな生息地に住むことができる。両生類は滑らかで湿った皮膚を持っているので、脅威にさらされたときに水の中に滑り落ちやすい。彼らは通常、水の中に卵を産み、そこで胚が孵化して成虫になる。</p>\r\n\r\n<p>両生類は食物網の重要な一部であり、魚類、鳥類、ヘビ類、哺乳類を含むさまざまな捕食者の餌であり、有機物の分解にも重要な役割を果たしている。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:32:49+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:33:05.034069+00:00")} ) 
    living_things_species_14.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_14 = importer.save_or_locate(living_things_species_14)

    living_things_species_15 = Species()
    living_things_species_15.name = '甲殻類'
    living_things_species_15.slug = 'crustacean-jp'
    living_things_species_15.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_species_15.article =  importer.locate_object(Article, "id", Article, "id", 166, {'id': 166, 'excerpt': '甲殻類', 'kicker': '甲殻類', 'content': '<p>甲殻類は、硬い外骨格と関節のある足を持つ海洋動物の一種で、塩分と淡水の両方で見られ、カニ、ロブスター、エビなどの生物が含まれる。</p>\r\n\r\n<p>甲殻類は海洋食物連鎖の重要な部分であり、大型動物の食物源であるとともに、海洋生態系のバランスを保つ役割も果たしている。</p>\r\n\r\n<p>カニは最も一般的な甲殻類である。世界各地で見られ、形や大きさもさまざまである。カニは塩分と淡水の両方に生息し、海底や川や小川の両方で見られる。</p>\r\n\r\n<p>ロブスターは、世界中の沿岸海域で見られるもう一つのタイプの甲殻類である。ロブスターは人気のある食品であり、淡水と塩水の両方で見られる。</p>\r\n\r\n<p>エビは甲殻類の中で最も小さく、塩分と淡水の両方に存在し、人気のある食品である。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:31:15+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:31:27.578162+00:00")} ) 
    living_things_species_15.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_15 = importer.save_or_locate(living_things_species_15)

    living_things_species_16 = Species()
    living_things_species_16.name = '軟体動物'
    living_things_species_16.slug = 'mollusk-jp'
    living_things_species_16.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_species_16.article =  importer.locate_object(Article, "id", Article, "id", 157, {'id': 157, 'excerpt': '軟体動物', 'kicker': '軟体動物', 'content': '<p>軟体動物は無脊椎動物の大きくて多様な門であり、約85,000種の軟体動物が記載されており、これは記載されている無脊椎動物の約3分の1を占めている。軟体動物にはカタツムリ、アサリ、タコ、イカなどが含まれる。</p>\r\n\r\n<p>軟体動物門は9つの綱に分けられる。</p>\r\n\r\n<p>腹足類は軟体動物の中で最大の綱であり、カタツムリとナメクジを含む。腹足類はらせん状にコイル状になった単一の殻をもつ。</p>\r\n\r\n<p>頭足類は軟体動物の中で2番目に大きな綱であり、タコとイカを含む。頭足類は8本の腕と2本の触手を特徴とする。</p>\r\n\r\n<p>二枚貝はアサリとムール貝を含む軟体動物の綱である。二枚貝は互いに蝶番で固定された2つの殻を特徴とする。</p>\r\n\r\n<p>scaphopodsは牙の殻を含む軟体動物の小さな綱である。Scaphopodsは細長い管状の殻を特徴とする。</p>\r\n\r\n<p>monoplacophoransは軟体動物の最も原始的なグループである軟体動物の小さな綱である。Monoplacophoransは湾曲した単一の殻を特徴とする。</p>\r\n\r\n<p>polyplacophoransはチトンを含む軟体動物の小さな綱である。Polyplacophoransは体を覆う8枚の重なり合った板を特徴とする。</p>\r\n\r\n<p>aplacophoransは殻のないことを特徴とする軟体動物の小さな綱である。Aplacophoransには虫のような軟体動物が含まれる。</p>\r\n\r\n<p>有櫛動物はクラゲに似た動物の小さな綱である。有櫛動物は8本の櫛のような触手を特徴とする。</p>\r\n\r\n<p>軟体動物は非常に多様で広範な動物群である。それらは海洋と淡水の両方の生息地で見られる。軟体動物は食物網の重要な部分であり、その生態系の生態学において役割を果たす。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:25:03+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:25:30.329169+00:00")} ) 
    living_things_species_16.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 8, {'id': 8, 'name': 'living-things/species'} ) 
    living_things_species_16 = importer.save_or_locate(living_things_species_16)

    # Re-processing model: living_things.models.Species

















