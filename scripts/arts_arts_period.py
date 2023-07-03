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
# manage.py dumpscript arts.ArtsPeriod
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

    # Processing model: arts.models.ArtsPeriod

    from arts.models import ArtsPeriod

    arts_artsperiod_1 = ArtsPeriod()
    arts_artsperiod_1.name = 'ancient_times'
    arts_artsperiod_1.slug = 'ancient_times'
    arts_artsperiod_1.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_1.period = None
    arts_artsperiod_1.article =  importer.locate_object(Article, "id", Article, "id", 105, {'id': 105, 'excerpt': 'Ancient', 'kicker': 'Ancient', 'content': '<p>Art during Ancient Times was created mainly for religious purposes. Many of the first artworks were made to decorate temples and honor the gods. Over time, however, art began to be created for other reasons, such as to celebrate historical events or to depict scenes from everyday life.</p>\r\n\r\n<p>Most of the art from Ancient Times is lost, so we know very little about it. However, we can get a glimpse of what it might have looked like from the few surviving artworks that have been excavated from archaeological sites.</p>\r\n\r\n<p>Most of the art from this period was made from materials such as stone, pottery, and metal. Designs were often carved or painted onto the surfaces of these objects.</p>\r\n\r\n<p>One of the most famous pieces of Ancient Egyptian art is the bust of Queen Nefertiti. This statue was carved from limestone in the 14th century BC and is now on display in the Neues Museum in Berlin, Germany.</p>\r\n\r\n<p>Another famous artwork from this period is the Sarcophagus of the couple, which was made from pink granite in the 4th century BC. This sarcophagus is now on display in the Vatican Museums in Rome, Italy.</p>\r\n\r\n<p>Art from the Classical period is perhaps best known for its sculptures. One of the most famous sculptures from this period is the marble statue of the Apollo of the Belvedere. This statue was made in the 1st century BC and is now on display in the Vatican Museums in Rome, Italy.</p>\r\n\r\n<p>During the Hellenistic period, art began to be influenced by the cultures of the East. This can be seen in the use of color and in the inclusion of images of animals and plants. One of the most famous examples of Hellenistic art is the Winged Victory of Samothrace. This statue was made in the 2nd century BC and is now on display in the Louvre Museum in Paris, France.</p>\r\n\r\n<p>The art of the Roman period is characterized by its realism and the use of perspective. One of the most famous pieces of Roman art is the statue of David. This statue was carved from marble in the 15th century BC and is now on display in the Accademia Gallery in Florence, Italy.</p>\r\n\r\n<p>The art of the Early Christian period is characterized by its simplicity and its use of symbols. One of the most famous examples of Early Christian art is the mosaic of the Madonna and Child. This mosaic was made in the 6th century AD and is now on display in the Basilica of San Vitale in Ravenna, Italy.</p>\r\n\r\n<p>During the Medieval period, art was often commissioned by the Church. The most famous example of Medieval art is the stained glass window of the Rose of Sharon. This window was created in the 12th century AD and is now on display in the Chartres Cathedral in Chartres, France.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T08:09:01+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T08:09:13.386695+00:00")} ) 
    arts_artsperiod_1.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_1 = importer.save_or_locate(arts_artsperiod_1)

    arts_artsperiod_2 = ArtsPeriod()
    arts_artsperiod_2.name = '古代'
    arts_artsperiod_2.slug = 'ancient_times-jp'
    arts_artsperiod_2.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_2.period = None
    arts_artsperiod_2.article =  importer.locate_object(Article, "id", Article, "id", 106, {'id': 106, 'excerpt': '古代', 'kicker': '古代', 'content': '<p>古代の芸術は主に宗教的な目的で作られました。最初の芸術作品の多くは、寺院を装飾し、神を称えるために作られました。しかし、時間の経過とともに、歴史的な出来事を祝うためや日常生活の場面を描くためなど、他の理由で芸術が作られるようになりました。</p>\r\n\r\n<p>古代の芸術のほとんどは失われているので、私たちはそれについてほとんど知りません。しかし、考古学的な遺跡から発掘された数少ない現存する芸術作品から、それがどのようなものであったかを垣間見ることができます。</p>\r\n\r\n<p>この時代の芸術のほとんどは、石、陶器、金属などの材料で作られていました。デザインは、これらのオブジェクトの表面に彫刻またはペイントされることがよくありました。</p>\r\n\r\n<p>古代エジプトの芸術の最も有名な作品の1つは、ネフェルティティ女王の胸像です。この像は紀元前14世紀に石灰岩から彫られたもので、現在ドイツのベルリンにあるヌーエス美術館に展示されています。</p>\r\n\r\n<p>この時代のもう1つの有名な芸術作品は、紀元前4世紀にピンクの花崗岩で作られた夫婦の石棺です。この石棺は現在、バチカン美術館に展示されています。</p>\r\n\r\n<p>古典時代の芸術は彫刻で最もよく知られています。この時代の最も有名な彫刻の1つは、ベルヴェデーレのアポロの大理石像です。この像は紀元前1世紀に作られ、現在はバチカン美術館に展示されています。</p>\r\n\r\n<p>ヘレニズムの時代になると、芸術は東洋の文化の影響を受け始めました。これは、色の使用や動植物のイメージの包含に見られます。ヘレニズム芸術の最も有名な例の1つは、サモトラケの翼のある勝利です。この像は紀元前2世紀に作られ、現在フランスのパリのルーブル美術館に展示されています。</p>\r\n\r\n<p>ローマ時代の芸術は、そのリアリズムと遠近法の使用によって特徴づけられる。ローマ美術の最も有名な作品の1つは、ダビデの像です。この像は紀元前15世紀に大理石から彫られたもので、現在イタリアのフィレンツェにあるアカデミアギャラリーに展示されています。</p>\r\n\r\n<p>初期キリスト教時代の芸術は、その簡潔さとシンボルの使用が特徴です。初期キリスト教芸術の最も有名な例の1つは、マドンナと子供のモザイクです。このモザイクは6世紀に作られ、現在、ラヴェンナのサン・ヴィターレ聖堂で展示されています。</p>\r\n\r\n<p>中世には、芸術はしばしば教会から委託された。中世の芸術の最も有名な例は、シャロンのバラのステンドグラスの窓である。この窓は12世紀に作られ、現在フランスのシャルトルのシャルトル大聖堂に展示されている。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T08:09:41+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T08:09:52.912673+00:00")} ) 
    arts_artsperiod_2.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_2 = importer.save_or_locate(arts_artsperiod_2)

    arts_artsperiod_3 = ArtsPeriod()
    arts_artsperiod_3.name = '500s_1300s'
    arts_artsperiod_3.slug = '500s-1300s'
    arts_artsperiod_3.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_3.period = None
    arts_artsperiod_3.article =  importer.locate_object(Article, "id", Article, "id", 107, {'id': 107, 'excerpt': '500s', 'kicker': '500s', 'content': '<p>Art during the 500s-1300s was greatly influenced by the beliefs and religions of the time. Religion played a big role in the art of the Byzantine Empire, the Islamic world, and the Christian world.</p>\r\n\r\n<p>In the Byzantine Empire, the official state religion was Christianity. Many of the Byzantine Empire&#39;s artworks depicted religious scenes and images. One of the most famous Byzantine artworks is the mosaic in the Church of San Vitale in Ravenna, Italy. The mosaic shows the Byzantine Emperor Justinian and his wife, Empress Theodora, with their retinue of courtiers.</p>\r\n\r\n<p>The Islamic world was founded in the 7th century, and the first Islamic dynasty, the Umayyads, ruled from 661-750. The Islamic world was greatly influenced by the Byzantine Empire, and many Islamic artworks featured Byzantine-style designs and motifs. One of the most famous Islamic artworks is the Dome of the Rock in Jerusalem. The Dome of the Rock is a shrine built in the late 7th century, and it features a beautiful mosaic dome.</p>\r\n\r\n<p>In the Christian world, the religion was divided into three branches: the Catholic Church, the Eastern Orthodox Church, and the Protestant Church. Each branch had its own distinct art style. The Catholic Church was the largest and most influential branch of Christianity, and its art was characterized by realism and the use of perspective. One of the most famous Catholic Church artworks is the Sistine Chapel ceiling, which was painted by Michelangelo in the 15th century. The Eastern Orthodox Church was less influential than the Catholic Church, and its art was characterized by geometric designs and a use of color to create a mystical effect. One of the most famous Eastern Orthodox Church artworks is the frescoes in the Church of the Holy Sepulcher in Jerusalem. The Protestant Church was founded in the 16th century, and its art was characterized by simplicity and a rejection of the ornate style of the Catholic and Eastern Orthodox Churches. One of the most famous Protestant Church artworks is the painting of the Last Supper by Leonardo da Vinci.</p>\r\n\r\n<p>In the 500s, the Byzantine Empire was the most powerful force in the Mediterranean, and its art was the most influential in the region. In the 600s, the Islamic world began to emerge as a powerful force, and its art began to have a significant impact on the art of the Byzantine Empire and the Christian world. In the 1000s, the Byzantine Empire began to decline in power, and the Islamic world became the dominant force in the Mediterranean. In the 1300s, the Islamic world began to decline in power, and the Byzantine Empire regained its dominance in the region.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T08:18:22+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T08:18:40.671269+00:00")} ) 
    arts_artsperiod_3.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_3 = importer.save_or_locate(arts_artsperiod_3)

    arts_artsperiod_4 = ArtsPeriod()
    arts_artsperiod_4.name = '500年代-1300年代'
    arts_artsperiod_4.slug = '500s-1300s-jp'
    arts_artsperiod_4.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_4.period = None
    arts_artsperiod_4.article =  importer.locate_object(Article, "id", Article, "id", 108, {'id': 108, 'excerpt': '500', 'kicker': '500', 'content': '<p>500年代から1300年代にかけての芸術は、当時の信仰や宗教に大きく影響された。宗教は、ビザンチン帝国、イスラム世界、キリスト教世界の芸術において大きな役割を果たした。</p>\r\n\r\n<p>ビザンチン帝国では、公式の国教はキリスト教であった。ビザンチン帝国の芸術作品の多くは、宗教的な場面やイメージを描いていた。最も有名なビザンチンの芸術作品の1つは、イタリアのラヴェンナにあるサン・ヴィターレ教会のモザイクです。モザイクには、ビザンチン帝国のユスティニアヌス皇帝とその妻であるテオドラ皇后が、廷臣の従者とともに描かれています。</p>\r\n\r\n<p>イスラム世界は7世紀に建国され、最初のイスラム王朝であるウマイヤ朝が661年から750年にかけて統治しました。イスラム世界はビザンチン帝国の影響を大きく受けており、多くのイスラム芸術作品はビザンチン様式のデザインやモチーフを特徴としていました。最も有名なイスラム芸術の1つは、エルサレムの岩のドームです。岩のドームは7世紀後半に建てられた神社で、美しいモザイクドームが特徴です。</p>\r\n\r\n<p>キリスト教の世界では、宗教はカトリック教会、東方正教会、プロテスタントの3つの宗派に分かれていました。それぞれの宗派には独自の芸術スタイルがありました。カトリック教会はキリスト教の最大かつ最も影響力のある宗派であり、その芸術はリアリズムと遠近法の使用によって特徴づけられました。最も有名なカトリック教会の芸術作品の1つは、15世紀にミケランジェロによって描かれたシスティーナ礼拝堂の天井です。東方正教会はカトリック教会ほど影響力がなく、その芸術は幾何学的なデザインと神秘的な効果を生み出すための色の使用によって特徴づけられました。最も有名な東方正教会の芸術作品の1つは、エルサレムの聖墳墓教会のフレスコ画です。プロテスタント教会は16世紀に設立され、その芸術はカトリックと東方正教会の華美なスタイルを拒絶する簡素さによって特徴づけられました。最も有名なプロテスタント教会の芸術作品の1つは、レオナルド・ダ・ヴィンチによる最後の晩餐の絵画です。</p>\r\n\r\n<p>500年代、ビザンチン帝国は地中海で最も強力な勢力であり、その芸術はこの地域で最も影響力があった。600年代には、イスラム世界が強力な勢力として台頭し始め、その芸術はビザンチン帝国の芸術とキリスト教世界に大きな影響を与え始めた。1000年代には、ビザンチン帝国の権力が衰退し始め、イスラム世界は地中海で支配的な勢力となった。1300年代には、イスラム世界の権力が衰退し始め、ビザンチン帝国はこの地域での支配を回復した。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T08:19:15+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T08:19:31.066212+00:00")} ) 
    arts_artsperiod_4.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_4 = importer.save_or_locate(arts_artsperiod_4)

    arts_artsperiod_5 = ArtsPeriod()
    arts_artsperiod_5.name = '1400s'
    arts_artsperiod_5.slug = '1400s'
    arts_artsperiod_5.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_5.period = None
    arts_artsperiod_5.article =  importer.locate_object(Article, "id", Article, "id", 109, {'id': 109, 'excerpt': '1400s', 'kicker': '1400s', 'content': '<p>During the 1400s, art was heavily influenced by the Renaissance, a cultural movement which began in Italy and celebrated the rediscovery of classical antiquity. This period also saw the rise of the humanist movement, which emphasised the importance of individualism and the study of classical literature and philosophy.</p>\r\n\r\n<p>One of the most famous artists of the 1400s was Donatello, who was renowned for his sculptures of religious subjects and for his innovative use of perspective in his paintings. Other notable artists of the period include Sandro Botticelli, whose famous painting the Birth of Venus is one of the most iconic images of the Renaissance, and Leonardo da Vinci, who was not only a painter but also a mathematician, engineer and scientist.</p>\r\n\r\n<p>In the 1400s, art was becoming increasingly secular, and was no longer solely used for religious purposes. This was reflected in the increasing popularity of portraits, which began to be commissioned not just by the aristocracy but also by the growing middle class.</p>\r\n\r\n<p>The art of the 1400s was also characterised by its realism and its attention to detail. This was particularly evident in the work of Leonardo da Vinci, whose paintings such as the Mona Lisa are renowned for their realistic portrayal of the human figure.</p>\r\n\r\n<p>In the 1400s, the use of perspective in art was also becoming more sophisticated, and artists were beginning to experiment with different techniques to create a sense of depth and realism. This was particularly evident in the work of Masaccio, who is considered to be the first artist to use linear perspective in his paintings.</p>\r\n\r\n<p>The 1400s was a period of great innovation in the world of art, and saw the emergence of some of the most famous and iconic artists of all time. It was a time of great change and growth, and the art of the period reflects this perfectly.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T08:20:10+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T08:20:29.143856+00:00")} ) 
    arts_artsperiod_5.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_5 = importer.save_or_locate(arts_artsperiod_5)

    arts_artsperiod_6 = ArtsPeriod()
    arts_artsperiod_6.name = '1400年代'
    arts_artsperiod_6.slug = '1400s-jp'
    arts_artsperiod_6.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_6.period = None
    arts_artsperiod_6.article =  importer.locate_object(Article, "id", Article, "id", 110, {'id': 110, 'excerpt': '1400年代', 'kicker': '1400年代', 'content': '<p>1400年代、芸術はイタリアで始まった古典の再発見を祝う文化運動であるルネッサンスの影響を強く受けた。この時期には、個人主義と古典文学と哲学の研究の重要性を強調したヒューマニスト運動も台頭した。</p>\r\n\r\n<p>1400年代の最も有名な芸術家の一人は、宗教的な主題の彫刻と絵画における革新的な視点の使用で有名なドナテッロであった。この時代の他の注目すべき芸術家には、ルネサンスの最も象徴的なイメージの一つであるヴィーナスの誕生を描いた有名な絵画で知られるサンドロ・ボッティチェッリや、画家であるだけでなく、数学者、技術者、科学者でもあったレオナルド・ダ・ヴィンチがいる。</p>\r\n\r\n<p>1400年代、芸術はますます世俗的になり、もはや宗教的な目的のためだけに使われることはなくなった。これは肖像画の人気の高まりに反映され、肖像画は貴族だけでなく、成長する中産階級によっても依頼されるようになった。</p>\r\n\r\n<p>1400年代の芸術はまた、そのリアリズムと細部への注意によって特徴づけられた。これは特にレオナルド・ダ・ヴィンチの作品で明らかであり、モナリザのような彼の絵は、人間の姿を写実的に描いたことで有名である。</p>\r\n\r\n<p>1400年代に入ると、遠近法の利用がより高度になり、奥行き感や臨場感を出すための様々な手法が試みられるようになったが、このことは、直線遠近法を初めて用いた画家とされるマサッチオの作品に顕著である。</p>\r\n\r\n<p>1400年代は、芸術の世界における大きな革新の時代であり、史上最も有名で象徴的な芸術家の出現を見た。それは大きな変化と成長の時代であり、この時代の芸術はこれを完全に反映している。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:04:50+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:05:06.573223+00:00")} ) 
    arts_artsperiod_6.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_6 = importer.save_or_locate(arts_artsperiod_6)

    arts_artsperiod_7 = ArtsPeriod()
    arts_artsperiod_7.name = '1500s'
    arts_artsperiod_7.slug = '1500s'
    arts_artsperiod_7.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_7.period = None
    arts_artsperiod_7.article =  importer.locate_object(Article, "id", Article, "id", 111, {'id': 111, 'excerpt': '1500s', 'kicker': '1500s', 'content': '<p>The 1500s were a time of great exploration and change. The art of the time reflects this, with new techniques and styles emerging.</p>\r\n\r\n<p>One of the most important developments of the 1500s was the invention of oil painting. This allowed artists to create more realistic paintings, with a greater range of colors.</p>\r\n\r\n<p>One of the most famous oil painters of the 1500s was Leonardo da Vinci. He was a master of using light and shadow to create realistic scenes.</p>\r\n\r\n<p>Another important development of the 1500s was the introduction of perspective. This allowed artists to create paintings that looked like three-dimensional scenes.</p>\r\n\r\n<p>Some of the most famous artists of the 1500s include Michelangelo, Raphael, and Titian. They were all masters of the new techniques and styles that were emerging during the time.</p>\r\n\r\n<p>The 1500s were a time of great change and development in art. This was reflected in the new techniques and styles that emerged during the time.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:05:59+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:06:28.475158+00:00")} ) 
    arts_artsperiod_7.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_7 = importer.save_or_locate(arts_artsperiod_7)

    arts_artsperiod_8 = ArtsPeriod()
    arts_artsperiod_8.name = '1500年代'
    arts_artsperiod_8.slug = '1500s-jp'
    arts_artsperiod_8.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_8.period = None
    arts_artsperiod_8.article =  importer.locate_object(Article, "id", Article, "id", 112, {'id': 112, 'excerpt': '1500年代', 'kicker': '1500年代', 'content': '<p>1500年代は、大きな探求と変化の時代でした。当時の芸術はこれを反映しており、新しい技術とスタイルが生まれています。</p>\r\n\r\n<p>1500年代の最も重要な発展の1つは、油絵の発明でした。これにより、芸術家はより現実的な絵画をより多くの色で描くことができました。</p>\r\n\r\n<p>1500年代の最も有名な油絵画家の1人はレオナルド・ダ・ヴィンチでした。彼は、光と影を使って現実的なシーンを作ることに長けていました。</p>\r\n\r\n<p>1500年代のもう1つの重要な発展は、遠近法の導入でした。これにより、芸術家は3次元のシーンのように見える絵画を作ることができました。</p>\r\n\r\n<p>1500年代の最も有名な芸術家には、ミケランジェロ、ラファエル、ティツィアーノ・ヴェチェッリオなどがいます。彼らはすべて、その時代に生まれつつあった新しい技術とスタイルの達人でした。</p>\r\n\r\n<p>1500年代は芸術の大きな変化と発展の時代でした。これは、その時代に生まれつつあった新しい技術とスタイルに反映されていました。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:06:53+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:07:11.268566+00:00")} ) 
    arts_artsperiod_8.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_8 = importer.save_or_locate(arts_artsperiod_8)

    arts_artsperiod_9 = ArtsPeriod()
    arts_artsperiod_9.name = '1600s'
    arts_artsperiod_9.slug = '1600s'
    arts_artsperiod_9.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_9.period = None
    arts_artsperiod_9.article =  importer.locate_object(Article, "id", Article, "id", 113, {'id': 113, 'excerpt': '1600s', 'kicker': '1600s', 'content': '<p>The 1600s were a time of great artistic development and change. The Baroque period, which lasted from the 1600s to the 1700s, was characterized by elaborate, dramatic, and emotional art. This period was a reaction against the reigning style of the Renaissance, which was more restrained and formal.</p>\r\n\r\n<p>One of the most famous Baroque artists was Peter Paul Rubens, who was known for his vibrant, energetic paintings. One of his most famous works is The Descent from the Cross, which is a dramatic depiction of Jesus&#39;s death.</p>\r\n\r\n<p>Another Baroque artist who was popular in the 1600s was Michelangelo Merisi da Caravaggio, who was known for his dramatic use of light and shadow. One of his most famous paintings is The Calling of St. Matthew, which features a dramatic light shining down on the saint.</p>\r\n\r\n<p>The art of the 1600s was not just limited to painting; it also included theater, music, and architecture. One of the most famous theaters of the 1600s was the Globe Theatre, which was built by Shakespeare and his company. The music of the 1600s was dominated by the Baroque style, which featured elaborate and emotional compositions. And the architecture of the 1600s was characterized by the use of tall, imposing spires and domes.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:07:43+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:08:20.649145+00:00")} ) 
    arts_artsperiod_9.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_9 = importer.save_or_locate(arts_artsperiod_9)

    arts_artsperiod_10 = ArtsPeriod()
    arts_artsperiod_10.name = '1600年代'
    arts_artsperiod_10.slug = '1600s-jp'
    arts_artsperiod_10.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_10.period = None
    arts_artsperiod_10.article =  importer.locate_object(Article, "id", Article, "id", 114, {'id': 114, 'excerpt': '1600年代', 'kicker': '1600年代', 'content': '<p>1600年代は、大きな芸術的発展と変化の時代であった。1600年代から1700年代にかけて続いたバロック時代は、精巧でドラマチックで感情的な芸術によって特徴づけられた。この時代は、より抑制された形式的なルネッサンスの支配的なスタイルに対する反応であった。</p>\r\n\r\n<p>最も有名なバロックの芸術家の一人は、活気に満ちた精力的な絵画で知られるピーテル・パウル・ルーベンスであった。彼の最も有名な作品の一つは、イエスの死を劇的に描いた「十字架からの降臨」である。</p>\r\n\r\n<p>1600年代に人気を博したもう一人のバロック画家、ミケランジェロ・メリシ・ダ・カラヴァッジョは、光と影のドラマチックな使い方で知られています。彼の最も有名な絵の1つは、聖人に劇的な光が降り注ぐことを特徴とする聖マタイの召命です。</p>\r\n\r\n<p>1600年代の芸術は絵画だけでなく、演劇、音楽、建築も含んでいました。1600年代の最も有名な劇場の1つは、シェークスピアと彼の会社によって建てられたグローブ・シアターでした。1600年代の音楽は、精巧で感情的な作曲を特徴とするバロック様式によって支配されていました。そして1600年代の建築は、高くて印象的な尖塔とドームの使用によって特徴づけられました。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:08:55+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:09:11.816149+00:00")} ) 
    arts_artsperiod_10.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_10 = importer.save_or_locate(arts_artsperiod_10)

    arts_artsperiod_11 = ArtsPeriod()
    arts_artsperiod_11.name = '1700s'
    arts_artsperiod_11.slug = '1700s'
    arts_artsperiod_11.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_11.period = None
    arts_artsperiod_11.article =  importer.locate_object(Article, "id", Article, "id", 115, {'id': 115, 'excerpt': '1700s', 'kicker': '1700s', 'content': '<p>In the 1700s, there was a large focus on neoclassicism in art. This was a movement that favored classical art styles, often featuring simple designs and muted colors. Many artists of the time sought to create pieces that would be appreciated by the masses, rather than just the wealthy.</p>\r\n\r\n<p>One of the most famous neoclassical artists was Jacques-Louis David. He is known for his paintings of historical events, such as The Death of Socrates and The Oath of the Horatii. These pieces often depict idealized figures in simple compositions, with an emphasis on the purity of the human form.</p>\r\n\r\n<p>Other neoclassical artists of the time include Antonio Canova and Jean-Auguste-Dominique Ingres. Canova is known for his sculptures of classical figures, such as the statue of Napoleon Bonaparte that is now on display in the Louvre. Ingres is known for his paintings of historical scenes, as well as his portraits, which often feature intricate details and precise lines.</p>\r\n\r\n<p>Many of the works created during the neoclassical period are still considered some of the most iconic art pieces in history. They continue to be studied and admired by artists and art lovers alike.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:09:40+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:09:55.734647+00:00")} ) 
    arts_artsperiod_11.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_11 = importer.save_or_locate(arts_artsperiod_11)

    arts_artsperiod_12 = ArtsPeriod()
    arts_artsperiod_12.name = '1700年代'
    arts_artsperiod_12.slug = '1700'
    arts_artsperiod_12.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_12.period = None
    arts_artsperiod_12.article =  importer.locate_object(Article, "id", Article, "id", 116, {'id': 116, 'excerpt': '1700年', 'kicker': '1700年', 'content': '<p>1700年代の芸術は新古典主義に重点が置かれていました。これは古典的な芸術スタイルを支持する運動であり、多くの場合、シンプルなデザインと控えめな色が特徴でした。当時の多くの芸術家は、富裕層だけでなく一般の人々にも喜ばれる作品を作ろうとしました。</p>\r\n\r\n<p>最も有名な新古典主義の芸術家の一人はジャック=ルイ・デヴィッドです。彼は「ソクラテスの死」や「ホラティウスの誓い」などの歴史的な出来事を描いたことで知られています。これらの作品はしばしば、人間の形の純粋さを強調して、理想化された人物を単純な構成で描いています。</p>\r\n\r\n<p>当時の新古典派の芸術家には、アントニオ・カノーヴァやジャン=オーギュスト=ドミニク・アングルなどがいます。カノバは、現在ルーブル美術館に展示されているナポレオン・ボナパルトの像など、古典的な人物の彫刻で知られています。アングルは、歴史的な場面を描いた絵画や、しばしば複雑な細部と正確な線を特徴とする肖像画で知られています。</p>\r\n\r\n<p>新古典時代に作られた作品の多くは、今でも歴史上最も象徴的な芸術作品の一つと考えられています。それらは、芸術家や芸術愛好家にも同様に研究され、賞賛され続けています。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:10:10+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:10:23.024222+00:00")} ) 
    arts_artsperiod_12.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_12 = importer.save_or_locate(arts_artsperiod_12)

    arts_artsperiod_13 = ArtsPeriod()
    arts_artsperiod_13.name = '1800s'
    arts_artsperiod_13.slug = '1800s'
    arts_artsperiod_13.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_13.period = None
    arts_artsperiod_13.article =  importer.locate_object(Article, "id", Article, "id", 117, {'id': 117, 'excerpt': '1800s', 'kicker': '1800s', 'content': '<p>The 1800s in art history is largely marked by Romanticism, an artistic movement characterized by its emphasis on emotion and intuition. This was a reaction against the rationalism of the Enlightenment period. Romantics believed in the innate goodness of humans and the power of the imagination. They sought to express their ideas through poetry, music, and painting.</p>\r\n\r\n<p>Many Romantic artists were inspired by nature. They sought to capture the power and beauty of the natural world in their work. They often used dramatic lighting and landscapes to create moods and feelings.</p>\r\n\r\n<p>One of the most famous Romantic painters is Caspar David Friedrich. His paintings often depict lone figures in natural settings, such as the forest or the sea. Friedrich believed that through art, people could come to understand the spiritual truths of the universe.</p>\r\n\r\n<p>Other Romantic painters include John Constable, who often painted landscapes of his native England, and Eug&egrave;ne Delacroix, who was known for his dramatic, colorful paintings of historical scenes.</p>\r\n\r\n<p>In the early 1800s, a new artistic movement called Neoclassicism began to gain popularity. Neoclassical artists looked to ancient Greece and Rome for inspiration. They sought to create works that were simple and elegant, with clean lines and classical proportions.</p>\r\n\r\n<p>One of the most famous Neoclassical painters is Jacques-Louis David. He is best known for his paintings of historical events, such as the French Revolution. Other Neoclassical artists include Antonio Canova and Jean-Auguste-Dominique Ingres.</p>\r\n\r\n<p>In the late 1800s, a new movement called Impressionism began to emerge. Impressionist artists sought to capture the fleeting effects of light and color. They often painted outdoor scenes, using quick, loose brushstrokes to capture the impression of the scene rather than its actual details.</p>\r\n\r\n<p>Some of the most famous Impressionist painters include Claude Monet, Pierre-Auguste Renoir, and Edgar Degas. Unlike the Neoclassical artists, who tended to work in isolation, the Impressionists formed a group that met regularly to discuss their work and exhibitions.</p>\r\n\r\n<p>By the end of the 1800s, a new movement called Art Nouveau was gaining popularity. Art Nouveau artists sought to create a new style that was free of the traditional rules of art. They used curved lines and organic shapes to create a look that was both decorative and harmonious.</p>\r\n\r\n<p>Some of the most famous Art Nouveau artists include Gustav Klimt, Henri de Toulouse-Lautrec, and Alphonse Mucha.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:11:08+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:11:31.190552+00:00")} ) 
    arts_artsperiod_13.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_13 = importer.save_or_locate(arts_artsperiod_13)

    arts_artsperiod_14 = ArtsPeriod()
    arts_artsperiod_14.name = '1800年代'
    arts_artsperiod_14.slug = '1800s-jp'
    arts_artsperiod_14.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_14.period = None
    arts_artsperiod_14.article =  importer.locate_object(Article, "id", Article, "id", 118, {'id': 118, 'excerpt': '1800年', 'kicker': '1800年', 'content': '<p>1800年代の美術史では、ロマン主義が大きな特徴となっている。ロマン主義は、感情と直感を重視することを特徴とする芸術運動である。これは、啓蒙時代の合理主義に対する反応であった。ロマン主義は、人間の生来の善良さと想像力の力を信じていた。彼らは詩、音楽、絵画を通じて自分たちの考えを表現しようとした。</p>\r\n\r\n<p>多くのロマン主義芸術家は自然に触発された。彼らは作品の中で自然界の力と美を捉えようとした。彼らはしばしば劇的な照明と風景を使って気分と感情を作り出した。</p>\r\n\r\n<p>最も有名なロマン派の画家の一人はカスパー・ダーヴィト・フリードリヒです。彼の絵には、森や海などの自然の中に孤独な人物が描かれていることが多いです。フリードリヒは、芸術を通じて、人々は宇宙の精神的真実を理解することができると信じていた。</p>\r\n\r\n<p>ロマン派の画家には他にも、故郷の風景をよく描いたジョン・コンスタブルや、ドラマチックでカラフルな歴史的風景の絵で知られるウジェーヌ・ドラクロワなどがいる。</p>\r\n\r\n<p>1800年代初頭には、新古典主義と呼ばれる新しい芸術運動が人気を博し始めました。新古典派の芸術家たちは、古代ギリシャやローマにインスピレーションを求めました。彼らは、すっきりとした線と古典的なプロポーションを持つ、シンプルでエレガントな作品を作ろうとしました。</p>\r\n\r\n<p>最も有名な新古典派の画家の一人は、フランス革命などの歴史的な出来事を描いたことで最もよく知られているジャック=ルイ・ダビデです。他の新古典派の芸術家には、アントニオ・カノーヴァやジャン=オーギュスト=ドミニク・アングルなどがいます。</p>\r\n\r\n<p>1800年代後半、印象派と呼ばれる新しい運動が起こり始めました。印象派の芸術家たちは、光と色の一時的な効果を捉えようとしました。彼らはしばしば屋外のシーンを描き、実際の細部ではなくシーンの印象を捉えるために、速くてゆったりとしたブラシストロークを使用しました。</p>\r\n\r\n<p>最も有名な印象派の画家には、クロード・モネ、ピエール=オーギュスト・ルノワール、エドガー・ドガなどがいます。新古典派の芸術家たちは孤立して仕事をする傾向があったが、印象派の芸術家たちはグループを結成し、定期的に会合を開いて彼らの仕事や展示について議論した。</p>\r\n\r\n<p>1800年代の終わりには、アール・ヌーボーと呼ばれる新しい運動が盛んになりました。アール・ヌーボーのアーティストたちは、伝統的な芸術のルールから解放された新しいスタイルを作ろうとしました。彼らは曲線と有機的な形を使って、装飾的で調和のとれた外観を作り出しました。</p>\r\n\r\n<p>最も有名なアール・ヌーヴォーの芸術家には、グスタフ・クリムト、アンリ・ド・トゥールーズ=ロートレック、アルフォンス・ミュシャなどがいる。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:11:58+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:12:11.382871+00:00")} ) 
    arts_artsperiod_14.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_14 = importer.save_or_locate(arts_artsperiod_14)

    arts_artsperiod_15 = ArtsPeriod()
    arts_artsperiod_15.name = '1900s'
    arts_artsperiod_15.slug = '1900s'
    arts_artsperiod_15.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_15.period = None
    arts_artsperiod_15.article =  importer.locate_object(Article, "id", Article, "id", 119, {'id': 119, 'excerpt': '1900s', 'kicker': '1900s', 'content': '<p>The art world in the early 1900s was in a state of flux. The traditional techniques of painting and sculpture were being challenged by new, avant-garde styles. This period also saw the rise of the Modernist movement, which sought to redefine the way art was made and experienced.</p>\r\n\r\n<p>In painting, the Impressionist style was giving way to Cubism, which deconstructed objects into geometric shapes. The Futurists were exploring new ways of representing motion and energy, while the Surrealists were creating works that were based on dreams and the subconscious. In sculpture, the Cubists were creating abstract pieces, while the Dadaists were making art out of everyday objects.</p>\r\n\r\n<p>The early 1900s also saw the birth of the Abstract Expressionist movement. This movement sought to express the inner emotions of the artist through abstract painting and sculpture. The best known Abstract Expressionist artists are Jackson Pollock and Mark Rothko.</p>\r\n\r\n<p>The art world in the early 1900s was exciting and constantly evolving. It was a time of great creativity and innovation, and the works of the Modernist artists continue to be influential to this day.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:12:36+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:12:48.540365+00:00")} ) 
    arts_artsperiod_15.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_15 = importer.save_or_locate(arts_artsperiod_15)

    arts_artsperiod_16 = ArtsPeriod()
    arts_artsperiod_16.name = '1900年代'
    arts_artsperiod_16.slug = '1900s-jp'
    arts_artsperiod_16.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_16.period = None
    arts_artsperiod_16.article =  importer.locate_object(Article, "id", Article, "id", 120, {'id': 120, 'excerpt': '1900年', 'kicker': '1900年', 'content': '<p>1900年代初頭の美術界は、伝統的な絵画や彫刻の技法が新しい前衛的なスタイルに挑戦されるという激動の時代でした。この時代には、芸術の作り方や体験の仕方を再定義しようとするモダニズム運動も起こりました。</p>\r\n\r\n<p>絵画では、印象派の様式がキュービズムに取って代わられつつありました。キュービズムは、物体を幾何学的な形に分解したものです。未来派は運動とエネルギーを表現する新しい方法を探求していましたが、シュールレアリスムは夢と潜在意識に基づいた作品を生み出していました。彫刻では、キュービストは抽象的な作品を生み出していましたが、ダダイズムは日常的なものから芸術を生み出していました。</p>\r\n\r\n<p>1900年代初頭には抽象表現主義運動も生まれました。この運動は、抽象絵画や彫刻を通じてアーティストの内面の感情を表現しようとしました。抽象表現主義のアーティストとして最もよく知られているのは、ジャクソン・ポロックとマーク・ロスコです。</p>\r\n\r\n<p>1900年代初頭の美術界は刺激的で、絶えず進化していました。それは偉大な創造性と革新の時代であり、モダニストの芸術家の作品は今日まで影響力を持ち続けています。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:13:07+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:13:17.981457+00:00")} ) 
    arts_artsperiod_16.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_16 = importer.save_or_locate(arts_artsperiod_16)

    arts_artsperiod_17 = ArtsPeriod()
    arts_artsperiod_17.name = '2000s'
    arts_artsperiod_17.slug = '2000s'
    arts_artsperiod_17.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_artsperiod_17.period = None
    arts_artsperiod_17.article =  importer.locate_object(Article, "id", Article, "id", 121, {'id': 121, 'excerpt': '2000s', 'kicker': '2000s', 'content': '<p>The art of the 2000s was marked by a renewed interest in traditional mediums such as painting and sculpture, as well as a proliferation of new media. Digital art, Internet art, and video art were among the most popular new forms. Although the art market crashed in the early years of the decade, it began to rebound in the mid-2000s. The resulting increase in prices for contemporary artworks led to a renewed focus on marketability by artists and galleries.</p>\r\n\r\n<p>In the early years of the 2000s, many artists embraced the digital and technological possibilities of new media. German artist Martin Kippenberger created a series of digital prints that combined his own photographs with appropriated images from the Internet. In 2001, American artist Cory Arcangel hacked a Nintendo game console to create a work that displayed the game Super Mario Brothers in its entirety on one screen.</p>\r\n\r\n<p>In the mid-2000s, the art market began to rebound, leading to a renewed focus on marketability by artists and galleries. This led to a trend of artists producing more marketable works, often in traditional mediums such as painting and sculpture. In 2006, Damien Hirst set the record for the most expensive work of art ever sold at auction with his painting &quot;For the Love of God.&quot;</p>\r\n\r\n<p>As the 2000s drew to a close, the art world began to anticipate the next big thing. Some art observers predicted that virtual reality and artificial intelligence would be the big trends of the next decade.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:13:45+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:14:03.770486+00:00")} ) 
    arts_artsperiod_17.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_17 = importer.save_or_locate(arts_artsperiod_17)

    arts_artsperiod_18 = ArtsPeriod()
    arts_artsperiod_18.name = '2000年代'
    arts_artsperiod_18.slug = '2000s-jp'
    arts_artsperiod_18.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_artsperiod_18.period = None
    arts_artsperiod_18.article =  importer.locate_object(Article, "id", Article, "id", 122, {'id': 122, 'excerpt': '2000年代', 'kicker': '2000年代', 'content': '<p>2000年代の芸術は、絵画や彫刻などの伝統的な媒体への新たな関心と、新しい媒体の急増によって特徴づけられた。デジタル芸術、インターネット芸術、ビデオ・アートは、最も人気のある新しい形態の一つであった。芸術市場はこの10年の初めに暴落したが、2000年代半ばに回復し始めた。その結果、現代美術の価格が上昇し、芸術家やギャラリーによる市場性に再び焦点が当てられるようになった。</p>\r\n\r\n<p>2000年代初頭には、多くのアーティストが新しいメディアのデジタルおよび技術的な可能性を受け入れました。ドイツのアーティスト、マルティン・キッペンベルガーは、自分の写真とインターネットからの適切な画像を組み合わせた一連のデジタルプリントを作成しました。2001年には、アメリカのアーティスト、コーリー・アーキャンジェルが任天堂のゲーム機をハッキングして、スーパーマリオブラザーズのゲーム全体を1つの画面に表示する作品を作成しました。</p>\r\n\r\n<p>2000年代半ばになると、美術品の市況が回復し、アーティストや画廊の市場性が改めて注目されるようになりました。これにより、アーティストは、絵画や彫刻などの従来の媒体で、より市場性のある作品を制作する傾向が生まれました。2006年、ダミアン・ハーストは「神の愛のために」という作品で、オークションで販売された美術品の中で最も高価な作品の記録を打ち立てました。</p>\r\n\r\n<p>2000年代が終わりに近づくにつれて、芸術界は次の大きなことを予測し始めた。一部の芸術評論家は、バーチャルリアリティと人工知能が次の10年の大きなトレンドになると予測した。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T09:14:21+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T09:14:37.162802+00:00")} ) 
    arts_artsperiod_18.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 6, {'id': 6, 'name': 'arts/periods'} ) 
    arts_artsperiod_18 = importer.save_or_locate(arts_artsperiod_18)

    # Re-processing model: arts.models.ArtsPeriod



















