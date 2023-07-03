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
# manage.py dumpscript foods.Ingredient
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

    # Processing model: foods.models.Ingredient

    from foods.models import Ingredient

    foods_ingredient_1 = Ingredient()
    foods_ingredient_1.name = 'fruits'
    foods_ingredient_1.slug = 'fruits'
    foods_ingredient_1.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    foods_ingredient_1.location = None
    foods_ingredient_1.article =  importer.locate_object(Article, "id", Article, "id", 123, {'id': 123, 'excerpt': 'Fruit', 'kicker': 'Fruit', 'content': '<p>Fruit is a term used for sweet, edible parts of plants that are normally eaten as desserts or snacks. The word &quot;fruit&quot; is also used for many other culinary items that are not botanically fruits, such as sweetmeats, puddings, pastries, and cakes. In botany, a fruit is the seed-bearing structure in flowering plants formed from the ovary after flowering.</p>\r\n\r\n<p>Fruits are the means by which flowering plants disperse their seeds. Many fruits, such as tomatoes and apples, are eaten as is. Others, such as strawberries, blueberries, and raspberries, are often used in pies, tarts, ice creams, and other desserts. Fruits also include bananas, grapes, oranges, pineapples, and strawberries.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:50:12+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:51:20.958983+00:00")} ) 
    foods_ingredient_1.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_1 = importer.save_or_locate(foods_ingredient_1)

    foods_ingredient_2 = Ingredient()
    foods_ingredient_2.name = 'vegetables'
    foods_ingredient_2.slug = 'vegetables'
    foods_ingredient_2.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    foods_ingredient_2.location = None
    foods_ingredient_2.article =  importer.locate_object(Article, "id", Article, "id", 130, {'id': 130, 'excerpt': 'Food', 'kicker': 'Food', 'content': '<p>Food of Vegetables</p>\r\n\r\n<p>Vegetables are dietary staples for many people all over the world. They are low in calories and high in fiber, vitamins, and minerals. They also contain phytochemicals, which are plant-based chemicals that may protect against cancer and other diseases. There are many different types of vegetables, and each one has its own unique flavor, texture, and nutritional profile.</p>\r\n\r\n<p>Some of the most popular vegetables include broccoli, cauliflower, collard greens, kale, lettuce, mushrooms, onions, peas, peppers, potatoes, spinach, and tomatoes. These vegetables can be eaten raw or cooked. They can be added to salads, sandwiches, and other dishes, or they can be eaten as standalone snacks.</p>\r\n\r\n<p>Most vegetables are low in calories and fat, but they are high in fiber. A cup of cooked broccoli, for example, contains only 38 calories and 2.5 grams of fat, but it provides 5 grams of fiber. A cup of cooked kale contains 36 calories and 2.5 grams of fat, but it provides 5 grams of fiber.</p>\r\n\r\n<p>Vegetables are also high in vitamins and minerals. A cup of cooked broccoli, for example, contains 135% of the daily value for vitamin C, 115% of the daily value for vitamin K, and 80% of the daily value for folate. A cup of cooked kale contains 550% of the daily value for vitamin A, 200% of the daily value for vitamin C, and 6% of the daily value for iron.</p>\r\n\r\n<p>Vegetables are also a good source of phytochemicals. A cup of cooked broccoli, for example, contains 18 milligrams of phytochemicals. A cup of cooked kale contains 8 milligrams of phytochemicals.</p>\r\n\r\n<p>Phytochemicals are plant-based chemicals that may protect against cancer and other diseases. Some of the most well-known phytochemicals include carotenoids, flavonoids, and lignans.</p>\r\n\r\n<p>Carotenoids are a group of red, orange, and yellow pigments found in many fruits and vegetables. They are especially high in carrots, sweet potatoes, and winter squash. Some of the most well-known carotenoids include beta-carotene, lutein, and lycopene.</p>\r\n\r\n<p>Flavonoids are a group of plant-based chemicals that are found in many fruits, vegetables, and herbs. They are especially high in berries, apples, onions, and tea. Some of the most well-known flavonoids include anthocyanins, catechins, and proanthocyanidins.</p>\r\n\r\n<p>Lignans are a group of phytochemicals that are found in many plants, including flaxseeds, sesame seeds, and legumes. Lignans are especially high in fiber. Some of the most well-known lignans include enterolactone and enterodiol.</p>\r\n\r\n<p>Vegetables are a healthy and delicious way to boost your intake of fiber, vitamins, minerals, and phytochemicals. They can be added to salads, sandwiches, and other dishes, or they can be eaten as standalone snacks.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:58:33+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:59:03.347346+00:00")} ) 
    foods_ingredient_2.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_2 = importer.save_or_locate(foods_ingredient_2)

    foods_ingredient_3 = Ingredient()
    foods_ingredient_3.name = 'meats'
    foods_ingredient_3.slug = 'meats'
    foods_ingredient_3.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    foods_ingredient_3.location = None
    foods_ingredient_3.article =  importer.locate_object(Article, "id", Article, "id", 135, {'id': 135, 'excerpt': 'meats', 'kicker': 'meats', 'content': '<p>The most common meats consumed in the U.S. are beef, pork, and chicken. The meats Americans eat can be classified into two categories: red meat and white meat.</p>\r\n\r\n<p>Red meat includes beef, pork, lamb, and goat. Beef is the most popular red meat in the U.S. Americans eat about 55 pounds of beef per person per year. The most popular cuts of beef are ground beef, steaks, and roasts. Pork is the second most popular red meat in the U.S. Americans eat about 44 pounds of pork per person per year. The most popular cuts of pork are ham, chops, and bacon. Lamb is the third most popular red meat in the U.S. Americans eat about 2 pounds of lamb per person per year. The most popular cuts of lamb are leg of lamb and rack of lamb. Goat is the least popular red meat in the U.S. Americans eat about 0.25 pounds of goat per person per year.</p>\r\n\r\n<p>White meat includes chicken, turkey, and fish. Chicken is the most popular white meat in the U.S. Americans eat about 83 pounds of chicken per person per year. The most popular cuts of chicken are boneless, skinless breast meat and wings. Turkey is the second most popular white meat in the U.S. Americans eat about 7 pounds of turkey per person per year. The most popular cuts of turkey are boneless, skinless breast meat and legs. Fish is the third most popular white meat in the U.S. Americans eat about 7 pounds of fish per person per year. The most popular types of fish are salmon, tuna, and cod.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:02:40+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:03:02.594018+00:00")} ) 
    foods_ingredient_3.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_3 = importer.save_or_locate(foods_ingredient_3)

    foods_ingredient_4 = Ingredient()
    foods_ingredient_4.name = 'dairy_products'
    foods_ingredient_4.slug = 'dairy-products'
    foods_ingredient_4.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    foods_ingredient_4.location = None
    foods_ingredient_4.article =  importer.locate_object(Article, "id", Article, "id", 128, {'id': 128, 'excerpt': 'Dairy products', 'kicker': 'Dairy products', 'content': '<p>Dairy products are produced from the milk of mammals, usually cows, sheep, or goats. Dairy products are often high in fat and protein and include items such as cheese, yogurt, and milk. They often have a characteristic flavor and aroma that comes from the milk itself and the processing that the dairy products undergo.</p>\r\n\r\n<p>Cheese is a dairy product that is made from the milk of cows, sheep, or goats. The milk is processed into cheese by adding rennet, a substance that causes the milk to coagulate. The cheese is then cut into small pieces and left to age. The flavor and aroma of cheese come from the milk itself and the aging process.</p>\r\n\r\n<p>There are many different types of cheese, each with its own unique flavor and aroma. Some common types of cheese include cheddar, brie, blue cheese, and Swiss cheese. Cheese is often eaten as a snack or served as a side dish. It can also be used in recipes to add flavor and richness.</p>\r\n\r\n<p>Yogurt is a dairy product that is made from the milk of cows, sheep, or goats. The milk is processed into yogurt by adding bacteria that causes the milk to coagulate. The yogurt is then left to age. The flavor and aroma of yogurt come from the milk itself and the bacteria that are used to make it.</p>\r\n\r\n<p>There are many different types of yogurt, each with its own unique flavor and aroma. Some common types of yogurt include fruit yogurt, Greek yogurt, and yogurt smoothies. Yogurt is often eaten as a snack or served as a side dish. It can also be used in recipes to add flavor and richness.</p>\r\n\r\n<p>Milk is a dairy product that is made from the milk of cows, sheep, or goats. The milk is processed into milk by adding rennet, a substance that causes the milk to coagulate. The milk is then left to age. The flavor and aroma of milk come from the milk itself and the aging process.</p>\r\n\r\n<p>There are many different types of milk, each with its own unique flavor and aroma. Some common types of milk include whole milk, reduced fat milk, and skim milk. Milk is often drunk as a beverage or used in recipes to add flavor and richness.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:55:18+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:55:32.864729+00:00")} ) 
    foods_ingredient_4.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_4 = importer.save_or_locate(foods_ingredient_4)

    foods_ingredient_5 = Ingredient()
    foods_ingredient_5.name = 'grains'
    foods_ingredient_5.slug = 'grains'
    foods_ingredient_5.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    foods_ingredient_5.location = None
    foods_ingredient_5.article = None
    foods_ingredient_5.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_5 = importer.save_or_locate(foods_ingredient_5)

    foods_ingredient_6 = Ingredient()
    foods_ingredient_6.name = 'eggs'
    foods_ingredient_6.slug = 'eggs'
    foods_ingredient_6.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    foods_ingredient_6.location = None
    foods_ingredient_6.article =  importer.locate_object(Article, "id", Article, "id", 132, {'id': 132, 'excerpt': '', 'kicker': '', 'content': '<p>I f you&#39;re looking for a quick and easy way to add some protein and healthy fats to your diet, eggs are a great option. They&#39;re also a versatile food that can be cooked in a variety of ways.</p>\r\n\r\n<p>Here are some tips for adding eggs to your diet:</p>\r\n\r\n<p>-Eggs are a good source of protein and can help you feel full after eating them.</p>\r\n\r\n<p>-Eggs are also a good source of omega-3 fatty acids, which are beneficial for your health.</p>\r\n\r\n<p>-Eggs are a versatile food and can be cooked in a variety of ways.</p>\r\n\r\n<p>-Eggs are a good source of choline, which is important for brain health.</p>\r\n\r\n<p>-The yolk of an egg contains important nutrients like vitamin D, vitamin B12, and phosphorus.</p>\r\n\r\n<p>-Eggs are a good source of selenium, which is beneficial for your immune system.</p>\r\n\r\n<p>-Eggs are a low-carbohydrate food and can be a good choice for people who are following a low-carbohydrate diet.</p>\r\n\r\n<p>-Eggs are a good source of lutein and zeaxanthin, which are beneficial for your eyes.</p>\r\n\r\n<p>-The cholesterol in eggs doesn&#39;t have a negative effect on your blood cholesterol levels.</p>\r\n\r\n<p>Here are some of the health benefits of eggs:</p>\r\n\r\n<p>-Eggs are a good source of protein, which is important for muscle growth and maintenance.</p>\r\n\r\n<p>-Eggs are a good source of omega-3 fatty acids, which are beneficial for your heart health.</p>\r\n\r\n<p>-Eggs are a good source of choline, which is important for brain health.</p>\r\n\r\n<p>-The yolk of an egg contains important nutrients like vitamin D, vitamin B12, and phosphorus.</p>\r\n\r\n<p>-Eggs are a good source of selenium, which is beneficial for your immune system.</p>\r\n\r\n<p>-Eggs are a low-carbohydrate food and can be a good choice for people who are following a low-carbohydrate diet.</p>\r\n\r\n<p>-Eggs are a good source of lutein and zeaxanthin, which are beneficial for your eyes.</p>\r\n\r\n<p>-The cholesterol in eggs doesn&#39;t have a negative effect on your blood cholesterol levels.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:59:33+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:59:55.697887+00:00")} ) 
    foods_ingredient_6.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_6 = importer.save_or_locate(foods_ingredient_6)

    foods_ingredient_7 = Ingredient()
    foods_ingredient_7.name = 'fish'
    foods_ingredient_7.slug = 'fish'
    foods_ingredient_7.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    foods_ingredient_7.location = None
    foods_ingredient_7.article =  importer.locate_object(Article, "id", Article, "id", 134, {'id': 134, 'excerpt': 'Fish', 'kicker': 'Fish', 'content': '<p>What are the benefits of Fish?</p>\r\n\r\n<p>Fish is a lean protein that is packed with nutrients, including omega-3 fatty acids, vitamin D, and selenium. A 3-ounce serving of cooked fish provides around 20 grams of protein and just over 200 calories. Fish is also low in saturated fat and a good source of minerals such as magnesium, potassium, and phosphorus.</p>\r\n\r\n<p>One of the key nutrients found in fish is omega-3 fatty acids. These fatty acids are beneficial for heart health and can also help to reduce the risk of chronic diseases such as cancer, arthritis, and diabetes. In addition, omega-3 fatty acids can improve cognitive function and help to protect the brain from age-related decline.</p>\r\n\r\n<p>Fish is also a good source of vitamin D, which is essential for strong bones and teeth. Vitamin D is also important for regulating the immune system and overall health.</p>\r\n\r\n<p>Selenium is another nutrient found in fish. Selenium is a mineral that is important for thyroid health and can help to protect the body from cancer.</p>\r\n\r\n<p>What are some types of Fish?</p>\r\n\r\n<p>There are many different types of fish that can be enjoyed, including salmon, tuna, tilapia, cod, and halibut. Salmon is a particularly healthy fish, as it is high in omega-3 fatty acids and vitamin D. Tuna is also a good source of omega-3 fatty acids, as well as protein and selenium. Tilapia is a mild-tasting fish that is low in calories and fat. Cod and halibut are both high in protein and low in fat.</p>\r\n\r\n<p>How do I cook Fish?</p>\r\n\r\n<p>Fish can be cooked in a number of ways, including baking, grilling, poaching, and frying. When cooking fish, it is important to avoid overcooking, as this can make the fish dry and tough. Fish is typically cooked when it flakes easily with a fork.</p>\r\n\r\n<p>What are some recipes that include Fish?</p>\r\n\r\n<p>There are many recipes that include fish, such as salmon burgers, tuna salad, and tilapia tacos. These recipes are all easy to prepare and are packed with nutrients.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:01:44+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:02:01.242290+00:00")} ) 
    foods_ingredient_7.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_7 = importer.save_or_locate(foods_ingredient_7)

    foods_ingredient_8 = Ingredient()
    foods_ingredient_8.name = 'beans'
    foods_ingredient_8.slug = 'beans'
    foods_ingredient_8.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    foods_ingredient_8.location = None
    foods_ingredient_8.article =  importer.locate_object(Article, "id", Article, "id", 124, {'id': 124, 'excerpt': 'Beans', 'kicker': 'Beans', 'content': '<p>Beans are a type of legume. There are many different types of beans, and they come in different colors, sizes, and shapes. They are all high in protein, fiber, and antioxidants, and they are low in fat and calories. Beans are a good source of minerals, such as potassium, magnesium, and zinc, and they are also a good source of vitamins, including vitamin C, vitamin K, and folate.</p>\r\n\r\n<p>Beans are a versatile food that can be eaten cooked or raw. They can be added to salads, soups, and stews, or they can be eaten as a side dish. Beans are also a great ingredient in vegetarian and vegan dishes.</p>\r\n\r\n<p>Some of the most popular types of beans include black beans, navy beans, pinto beans, and white beans. Beans are available year-round and can be found in most grocery stores.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:51:59+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:52:32.266952+00:00")} ) 
    foods_ingredient_8.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_8 = importer.save_or_locate(foods_ingredient_8)

    foods_ingredient_9 = Ingredient()
    foods_ingredient_9.name = '果物'
    foods_ingredient_9.slug = 'fruits-jp'
    foods_ingredient_9.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    foods_ingredient_9.location = None
    foods_ingredient_9.article =  importer.locate_object(Article, "id", Article, "id", 126, {'id': 126, 'excerpt': '果実', 'kicker': '果実', 'content': '<p>果実は、通常デザートやスナックとして食べられる植物の甘くて食べられる部分に対して用いられる用語である。「果実」という語は、砂糖菓子、プリン、ペストリー、ケーキなど、植物の果実ではない他の多くの料理にも用いられる。植物学では、果実は、開花後に子房から形成される顕花植物の種子をつける構造である。</p>\r\n\r\n<p>果実は、顕花植物が種子を分散させる手段である。トマトやリンゴなどの多くの果実はそのまま食べられる。イチゴ、ブルーベリー、ラズベリーなどの他の果実は、パイ、タルト、アイスクリーム、その他のデザートによく用いられる。果実には、バナナ、ブドウ、オレンジ、パイナップル、イチゴなども含まれる。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:53:27+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:53:38.304137+00:00")} ) 
    foods_ingredient_9.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_9 = importer.save_or_locate(foods_ingredient_9)

    foods_ingredient_10 = Ingredient()
    foods_ingredient_10.name = '野菜'
    foods_ingredient_10.slug = 'vegetables-jp'
    foods_ingredient_10.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    foods_ingredient_10.location = None
    foods_ingredient_10.article =  importer.locate_object(Article, "id", Article, "id", 131, {'id': 131, 'excerpt': '野菜', 'kicker': '野菜', 'content': '<p>野菜は世界中の多くの人々の主食です。低カロリーで、繊維、ビタミン、ミネラルが豊富です。また、植物性化学物質も含まれています。植物性化学物質は、がんやその他の病気を予防する可能性のある植物由来の化学物質です。野菜には多くの種類があり、それぞれに独自の風味、食感、栄養特性があります。</p>\r\n\r\n<p>最も人気のある野菜には、ブロッコリー、カリフラワー、コラードグリーン、ケール、レタス、キノコ、タマネギ、エンドウ豆、コショウ、ジャガイモ、ホウレンソウ、トマトなどがあります。これらの野菜は生でも調理しても食べられます。サラダやサンドイッチなどの料理に加えたり、独立したおやつとして食べたりすることができます。</p>\r\n\r\n<p>ほとんどの野菜はカロリーと脂肪が少ないですが、繊維質が多く含まれています。例えば、調理されたブロッコリー1カップには、38カロリーと2.5グラムの脂肪しか含まれていませんが、繊維質は5グラム含まれています。調理されたケール1カップには、36カロリーと2.5グラムの脂肪が含まれていますが、繊維質は5グラム含まれています。</p>\r\n\r\n<p>野菜にはビタミンやミネラルも豊富に含まれています。例えば、調理したブロッコリー1カップには、ビタミンCが1日の摂取量の135%、ビタミンKが1日の摂取量の115%、葉酸が1日の摂取量の80%、調理したケール1カップには、ビタミンAが1日の摂取量の550%、ビタミンCが1日の摂取量の200%、鉄が1日の摂取量の6%含まれています。</p>\r\n\r\n<p>野菜にも植物性化学物質が豊富に含まれています。例えば、調理したブロッコリー1カップには18ミリグラムの植物性化学物質が含まれています。調理したケール1カップには8ミリグラムの植物性化学物質が含まれています。</p>\r\n\r\n<p>植物性化学物質は、がんやその他の疾患を予防する可能性のある植物由来の化学物質であり、最もよく知られている植物性化学物質には、カロテノイド、フラボノイド、リグナンなどがある。</p>\r\n\r\n<p>カロテノイドは、多くの果物や野菜に含まれる赤色、オレンジ色、黄色の色素である。特にニンジン、サツマイモ、冬カボチャに多く含まれている。最もよく知られているカロテノイドには、ベータカロテン、ルテイン、リコペンなどがある。</p>\r\n\r\n<p>フラボノイドは植物由来の化学物質で、多くの果物、野菜、ハーブに含まれています。特にベリー類、リンゴ、タマネギ、茶に多く含まれています。最もよく知られているフラボノイドには、アントシアニン、カテキン、プロアントシアニジンなどがあります。</p>\r\n\r\n<p>リグナンは、亜麻仁、ゴマ種子、マメ科植物を含む多くの植物に含まれる植物性化学物質のグループである。リグナンは特に繊維質が多く、最もよく知られているリグナンには、エンテロラクトンやエンテロジオールがある。</p>\r\n\r\n<p>野菜は、食物繊維、ビタミン、ミネラル、植物性化学物質の摂取量を増やすための健康的でおいしい方法です。サラダやサンドイッチなどの料理に加えたり、単体のおやつとして食べたりすることができます。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:59:11+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:59:27.154913+00:00")} ) 
    foods_ingredient_10.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_10 = importer.save_or_locate(foods_ingredient_10)

    foods_ingredient_11 = Ingredient()
    foods_ingredient_11.name = '肉'
    foods_ingredient_11.slug = 'meats-jp'
    foods_ingredient_11.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    foods_ingredient_11.location = None
    foods_ingredient_11.article =  importer.locate_object(Article, "id", Article, "id", 136, {'id': 136, 'excerpt': '肉', 'kicker': '肉', 'content': '<p>米国で最も一般的に消費される肉は牛肉、豚肉、鶏肉である。米国人が食べる肉は、赤肉と白肉の2つのカテゴリーに分類できる。</p>\r\n\r\n<p>赤肉には牛肉、豚肉、ラム肉、ヤギ肉が含まれる。牛肉は米国で最も人気のある赤肉である。米国人は1人当たり年間約55ポンドの牛肉を食べる。最も人気のある牛肉の部位は、ひき肉、ステーキ、ローストである。豚肉は米国で2番目に人気のある赤肉である。米国人は1人当たり年間約44ポンドの豚肉を食べる。最も人気のある豚肉の部位は、ハム、チョップ、ベーコンである。ラムは米国で3番目に人気のある赤肉である。米国人は1人当たり年間約2ポンドのラムを食べる。最も人気のあるラムの部位は、ラムの足とラムのラックである。ヤギは米国で最も人気のない赤肉である。米国人は1人当たり年間約0.25ポンドのヤギを食べる。</p>\r\n\r\n<p>白身肉には、鶏肉、七面鳥、魚が含まれます。鶏肉はアメリカで最も人気のある白身肉です。アメリカ人は1人当たり年間約83ポンドの鶏肉を食べます。鶏肉の最も人気のある部位は、骨なしで皮のない胸肉と手羽先です。七面鳥はアメリカで2番目に人気のある白身肉です。アメリカ人は1人当たり年間約7ポンドの七面鳥を食べます。七面鳥の最も人気のある部位は、骨なしで皮のない胸肉と足です。魚はアメリカで3番目に人気のある白身肉です。アメリカ人は1人当たり年間約7ポンドの魚を食べます。最も人気のある魚の種類は、サケ、マグロ、タラです。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:03:07+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:03:21.222697+00:00")} ) 
    foods_ingredient_11.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_11 = importer.save_or_locate(foods_ingredient_11)

    foods_ingredient_12 = Ingredient()
    foods_ingredient_12.name = '乳製品'
    foods_ingredient_12.slug = 'dairy-products-jp'
    foods_ingredient_12.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    foods_ingredient_12.location = None
    foods_ingredient_12.article =  importer.locate_object(Article, "id", Article, "id", 127, {'id': 127, 'excerpt': '乳製品', 'kicker': '乳製品', 'content': '<p>乳製品は、哺乳類(通常はウシ、ヒツジ、ヤギ)の乳から製造されます。乳製品は脂肪やタンパク質が多く、チーズ、ヨーグルト、牛乳などが含まれます。多くの場合、牛乳自体と乳製品が受ける加工に由来する独特の風味と香りがあります。</p>\r\n\r\n<p>チーズは、ウシ、ヒツジ、ヤギの乳から製造される乳製品です。牛乳は、乳を凝固させる物質であるレンネットを添加することによってチーズに加工されます。その後、チーズは小さく切断され、熟成されます。チーズの風味と香りは、牛乳自体と熟成過程に由来します。</p>\r\n\r\n<p>チーズにはいろいろな種類があり、それぞれに独特の風味と香りがあります。一般的な種類のチーズには、チェダーチーズ、ブリーチーズ、ブルーチーズ、スイスチーズなどがあります。チーズはおやつや付け合わせとしてよく食べられます。また、レシピに入れて風味とコクを加えることもできます。</p>\r\n\r\n<p>ヨーグルトは、牛や羊、山羊などの乳から作られた乳製品です。乳を凝固させる細菌を加えてヨーグルトに加工し、熟成させたものです。ヨーグルトの風味と香りは、乳そのものとそれを作るために使われた細菌からもたらされます。</p>\r\n\r\n<p>ヨーグルトにはさまざまな種類があり、それぞれに独特の風味と香りがあります。一般的な種類のヨーグルトには、フルーツヨーグルト、ギリシャヨーグルト、ヨーグルトスムージーなどがあります。ヨーグルトはおやつや付け合わせとしてよく食べられます。また、レシピに入れて風味とコクを加えることもできます。</p>\r\n\r\n<p>牛乳は、牛、羊、山羊の乳を原料とし、乳を凝固させる物質であるレンネットを加えて乳に加工し、熟成させた乳製品です。牛乳の風味や香りは、牛乳そのものと熟成の過程から生まれます。</p>\r\n\r\n<p>牛乳にはさまざまな種類があり、それぞれに独特の風味と香りがあります。一般的な種類の牛乳には、全乳、低脂肪乳、脱脂乳などがあります。牛乳は、風味と豊かさを加えるために、飲料として飲まれたり、レシピに使われたりすることがよくあります。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:54:36+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:55:06.232652+00:00")} ) 
    foods_ingredient_12.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_12 = importer.save_or_locate(foods_ingredient_12)

    foods_ingredient_13 = Ingredient()
    foods_ingredient_13.name = '穀物'
    foods_ingredient_13.slug = 'grains-jp'
    foods_ingredient_13.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    foods_ingredient_13.location = None
    foods_ingredient_13.article = None
    foods_ingredient_13.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_13 = importer.save_or_locate(foods_ingredient_13)

    foods_ingredient_14 = Ingredient()
    foods_ingredient_14.name = '卵'
    foods_ingredient_14.slug = 'eggs-jp'
    foods_ingredient_14.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    foods_ingredient_14.location = None
    foods_ingredient_14.article =  importer.locate_object(Article, "id", Article, "id", 133, {'id': 133, 'excerpt': '卵', 'kicker': '卵', 'content': '<p>手軽にタンパク質やヘルシーな脂肪を摂取したい人には、卵がおすすめです。また、さまざまな調理法で調理できる万能な食品でもあります。</p>\r\n\r\n<p>ここでは、卵を食事に加えるためのヒントをいくつか紹介します。</p>\r\n\r\n<p>-卵はタンパク質の良い供給源であり、食べた後に満腹感を感じるのに役立ちます。</p>\r\n\r\n<p>-卵はまた、健康に有益なオメガ3脂肪酸の良い供給源でもあります。</p>\r\n\r\n<p>-卵は多用途の食品であり、様々な方法で調理できます。</p>\r\n\r\n<p>-卵は脳の健康に重要なコリンの良い供給源です。</p>\r\n\r\n<p>-卵の卵黄には、ビタミンD、ビタミンB12、リンなどの重要な栄養素が含まれています。</p>\r\n\r\n<p>-卵は、免疫系に有益なセレンの良い供給源です。</p>\r\n\r\n<p>-卵は低炭水化物食品であり、低炭水化物食を遵守している人には良い選択となり得る。</p>\r\n\r\n<p>-卵は、目に有益なルテインおよびゼアキサンチンの良い供給源です。</p>\r\n\r\n<p>-卵に含まれるコレステロールは、血中コレステロール値に悪影響を及ぼさない。</p>\r\n\r\n<p>卵の健康効果のいくつかを以下に示します:</p>\r\n\r\n<p>-卵はタンパク質の優れた供給源であり、筋肉の成長と維持に重要である。</p>\r\n\r\n<p>-卵は心臓の健康に有益なオメガ3脂肪酸の優れた供給源である。</p>\r\n\r\n<p>-卵は脳の健康に重要なコリンの優れた供給源である。</p>\r\n\r\n<p>-卵の卵黄には、ビタミンD、ビタミンB12、リンなどの重要な栄養素が含まれている。</p>\r\n\r\n<p>-卵は、免疫系に有益なセレンの優れた供給源である。</p>\r\n\r\n<p>-卵は低炭水化物食品であり、低炭水化物食を遵守している人には良い選択となり得る。</p>\r\n\r\n<p>-卵は、目に有益なルテインおよびゼアキサンチンの優れた供給源である。</p>\r\n\r\n<p>-卵に含まれるコレステロールは、血中コレステロール値に悪影響を及ぼさない。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:00:11+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:00:36.019711+00:00")} ) 
    foods_ingredient_14.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_14 = importer.save_or_locate(foods_ingredient_14)

    foods_ingredient_15 = Ingredient()
    foods_ingredient_15.name = '魚'
    foods_ingredient_15.slug = 'fish-jp'
    foods_ingredient_15.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    foods_ingredient_15.location = None
    foods_ingredient_15.article =  importer.locate_object(Article, "id", Article, "id", 129, {'id': 129, 'excerpt': '魚', 'kicker': '魚', 'content': '<p>魚は、オメガ3脂肪酸、ビタミンD、セレンなどの栄養素が豊富な赤身のタンパク質です。3オンスの調理された魚は、約20グラムのタンパク質と200カロリー強を提供します。魚はまた、飽和脂肪が少なく、マグネシウム、カリウム、リンなどのミネラルの良い供給源でもあります。</p>\r\n\r\n<p>魚に含まれる重要な栄養素の1つはオメガ3脂肪酸です。これらの脂肪酸は心臓の健康に有益であり、がん、関節炎、糖尿病などの慢性疾患のリスクを低下させるのにも役立ちます。さらに、オメガ3脂肪酸は認知機能を改善し、加齢に伴う低下から脳を保護するのにも役立ちます。</p>\r\n\r\n<p>魚はまた、骨や歯を強くするために不可欠なビタミンDの良い供給源でもあります。ビタミンDは、免疫系および全体的な健康を調節するためにも重要である。</p>\r\n\r\n<p>セレンは魚に含まれるもう1つの栄養素です。セレンは甲状腺の健康に重要なミネラルであり、がんから体を守るのに役立ちます。</p>\r\n\r\n<p>魚の種類には何がありますか?</p>\r\n\r\n<p>サケ、マグロ、ティラピア、タラ、オヒョウなど、さまざまな種類の魚を楽しむことができます。サケはオメガ3脂肪酸とビタミンDが豊富で、特に健康的な魚です。マグロはオメガ3脂肪酸のほか、タンパク質とセレンも豊富です。ティラピアはカロリーと脂肪が少なく、まろやかな味の魚です。タラとオヒョウはタンパク質が多く、脂肪が少ないです。</p>\r\n\r\n<p>魚はどうやって調理するのですか?</p>\r\n\r\n<p>魚は、焼いたり、焼いたり、密漁したり、揚げたりするなど、さまざまな方法で調理できます。魚を調理するときは、加熱しすぎないことが重要です。加熱しすぎると、魚がパサパサして硬くなることがあります。魚は通常、フォークで簡単にフレークになると調理されます。</p>\r\n\r\n<p>魚を含むいくつかのレシピは何ですか?</p>\r\n\r\n<p>サーモンバーガー、ツナサラダ、ティラピアタコスなど、魚を含む多くのレシピがあります。これらのレシピはすべて、調理が簡単で、栄養が豊富です。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:55:41+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:56:41.827717+00:00")} ) 
    foods_ingredient_15.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_15 = importer.save_or_locate(foods_ingredient_15)

    foods_ingredient_16 = Ingredient()
    foods_ingredient_16.name = '豆'
    foods_ingredient_16.slug = 'beans-jp'
    foods_ingredient_16.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    foods_ingredient_16.location = None
    foods_ingredient_16.article =  importer.locate_object(Article, "id", Article, "id", 125, {'id': 125, 'excerpt': '豆', 'kicker': '豆', 'content': '<p>豆はマメ科植物の一種です。豆には多くの種類があり、色、大きさ、形が異なります。それらはすべてタンパク質、繊維、抗酸化物質が多く、脂肪とカロリーが低いです。豆はカリウム、マグネシウム、亜鉛などのミネラルの良い供給源であり、ビタミンC、ビタミンK、葉酸などのビタミンの良い供給源でもあります。</p>\r\n\r\n<p>豆は、調理しても生でも食べられる万能の食品です。サラダやスープ、シチューに加えたり、副菜として食べたりすることができます。豆は、ベジタリアンやビーガンの料理にも最適な材料です。</p>\r\n\r\n<p>最も一般的な種類の豆には、黒豆、紺豆、ピント豆、白豆などがあります。豆は一年中入手可能で、ほとんどの食料品店で見つけることができます。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T12:52:49+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T12:53:10.102204+00:00")} ) 
    foods_ingredient_16.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 11, {'id': 11, 'name': 'foods/ingredients'} ) 
    foods_ingredient_16 = importer.save_or_locate(foods_ingredient_16)

    # Re-processing model: foods.models.Ingredient

















