import string
import re
def preprocessing(text):
    # remove non-ASCII characters
    text = text.encode("ascii", "ignore").decode()
    # remove newlines and extra whitespace
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    # Remove Roman numerals
    text = re.sub(r'\b[MDCLXVI]+\b', '', text)

    # remove URLs
    text = re.sub(r"http\S+", "", text)

    # remove email addresses
    text = re.sub(r"\S+@\S+", "", text)
    
    # remove special characters and digits
    text = re.sub(r"[^A-Za-z\.]+", " ", text)
    text = text.lower()
    text = text.split(". ")
   
    # Add <s> and </s> to the beginning and end of each sentence
    text = ["<s>" + sentence.strip() + " </s>" for sentence in text]
    text = [sentence.split() for sentence in text]
    return text



# # Convert tokens to integer IDs
# def tokens_to_ids(tokens, vocab):
#     ids = []
#     for token in tokens:
#         if token in vocab:
#             ids.append(vocab[token])
#         else:
#             ids.append(vocab["<unk>"])
#     return ids


# # Create a vocabulary and map tokens to IDs
# def create_vocab(data):
#     print(type(data))
#     vocab = {"<pad>": 0, "<unk>": 1, "<s>": 2, "</s>": 3}
#     for sentence in data:
#         tokens = tokenize(sentence)
#         for token in tokens:
#             if token not in vocab:
#                 vocab[token] = len(vocab)
#     return vocab


# # Preprocess the data
# def preprocess(data):
#     vocab = create_vocab(data)
#     preprocessed = []
#     for sentence in data:
#         tokens = tokenize(sentence)
#         ids = tokens_to_ids(tokens, vocab)
#         preprocessed.append(ids)
#     return preprocessed, vocab



print(preprocessing('''= Valkyria Chronicles III = 
 
 Senjō no Valkyria 3 : Unrecorded Chronicles ( Japanese : 戦場のヴァルキュリア3 , lit . Valkyria of the Battlefield 3 ) , commonly referred to as Valkyria Chronicles III outside Japan , is a tactical role @-@ playing video game developed by Sega and Media.Vision for the PlayStation Portable . Released in January 2011 in Japan , it is the third game in the Valkyria series . Employing the same fusion of tactical and real @-@ time gameplay as its predecessors , the story runs parallel to the first game and follows the " Nameless " , a penal military unit serving the nation of Gallia during the Second Europan War who perform secret black operations and are pitted against the Imperial unit " Calamaty Raven " . 
 The game began development in 2010 , carrying over a large portion of the work done on Valkyria Chronicles II . While it retained the standard features of the series , it also underwent multiple adjustments , such as making the game more forgiving for series newcomers . Character designer Raita Honjou and composer Hitoshi Sakimoto both returned from previous entries , along with Valkyria Chronicles II director Takeshi Ozawa . A large team of writers handled the script . The game 's opening theme was sung by May 'n . 
 It met with positive sales in Japan , and was praised by both Japanese and western critics . After release , it received downloadable content , along with an expanded edition in November of that year . It was also adapted into manga and an original video animation series . Due to low sales of Valkyria Chronicles II , Valkyria Chronicles III was not localized , but a fan translation compatible with the game 's expanded edition was released in 2014 . Media.Vision would return to the franchise with the development of Valkyria : Azure Revolution for the PlayStation 4 . 
 
 = = Gameplay = = 
 
 As with previous Valkyira Chronicles games , Valkyria Chronicles III is a tactical role @-@ playing game where players take control of a military unit and take part in missions against enemy forces . Stories are told through comic book @-@ like panels with animated character portraits , with characters speaking partially through voiced speech bubbles and partially through unvoiced text . The player progresses through a series of linear missions , gradually unlocked as maps that can be freely scanned through and replayed as they are unlocked . The route to each story location on the map varies depending on an individual player 's approach : when one option is selected , the other is sealed off to the player . Outside missions , the player characters rest in a camp , where units can be customized and character growth occurs . Alongside the main story missions are character @-@ specific sub missions relating to different squad members . After the game 's completion , additional episodes are unlocked , some of them having a higher difficulty than those found in the rest of the game . There are also love simulation elements related to the game 's two main heroines , although they take a very minor role . 
 The game 's battle system , the BliTZ system , is carried over directly from Valkyira Chronicles . During missions , players select each unit using a top @-@ down perspective of the battlefield map : once a character is selected , the player moves the character around the battlefield in third @-@ person . A character can only act once per @-@ turn , but characters can be granted multiple turns at the expense of other characters ' turns . Each character has a field and distance of movement limited by their Action Gauge . Up to nine characters can be assigned to a single mission . During gameplay , characters will call out if something happens to them , such as their health points ( HP ) getting low or being knocked out by enemy attacks . Each character has specific " Potentials " , skills unique to each character . They are divided into " Personal Potential " , which are innate skills that remain unaltered unless otherwise dictated by the story and can either help or impede a character , and " Battle Potentials " , which are grown throughout the game and always grant boons to a character . To learn Battle Potentials , each character has a unique " Masters Table " , a grid @-@ based skill table that can be used to acquire and link different skills . Characters also have Special Abilities that grant them temporary boosts on the battlefield : Kurt can activate " Direct Command " and move around the battlefield without depleting his Action Point gauge , the character Reila can shift into her " Valkyria Form " and become invincible , while Imca can target multiple enemy units with her heavy weapon . 
 Troops are divided into five classes : Scouts , Shocktroopers , Engineers , Lancers and Armored Soldier . Troopers can switch classes by changing their assigned weapon . Changing class does not greatly affect the stats gained while in a previous class . With victory in battle , experience points are awarded to the squad , which are distributed into five different attributes shared by the entire squad , a feature differing from early games ' method of distributing to different unit types . 
 
 = = Plot = = 
 
 The game takes place during the Second Europan War . Gallian Army Squad 422 , also known as " The Nameless " , are a penal military unit composed of criminals , foreign deserters , and military offenders whose real names are erased from the records and thereon officially referred to by numbers . Ordered by the Gallian military to perform the most dangerous missions that the Regular Army and Militia will not do , they are nevertheless up to the task , exemplified by their motto , Altaha Abilia , meaning " Always Ready . " The three main characters are No.7 Kurt Irving , an army officer falsely accused of treason who wishes to redeem himself ; Ace No.1 Imca , a female Darcsen heavy weapons specialist who seeks revenge against the Valkyria who destroyed her home ; and No.13 Riela Marcellis , a seemingly jinxed young woman who is unknowingly a descendant of the Valkyria . Together with their fellow squad members , these three are tasked to fight against a mysterious Imperial unit known as Calamity Raven , consisting of mostly Darcsen soldiers . 
 As the Nameless officially do not exist , the upper echelons of the Gallian Army exploit the concept of plausible deniability in order to send them on missions that would otherwise make Gallia lose face in the war . While at times this works to their advantage , such as a successful incursion into Imperial territory , other orders cause certain members of the 422nd great distress . One such member , Gusurg , becomes so enraged that he abandons his post and defects into the ranks of Calamity Raven , attached to the ideal of Darcsen independence proposed by their leader , Dahau . At the same time , elements within Gallian Army Command move to erase the Nameless in order to protect their own interests . Hounded by both allies and enemies , and combined with the presence of a traitor within their ranks , the 422nd desperately move to keep themselves alive while at the same time fight to help the Gallian war effort . This continues until the Nameless 's commanding officer , Ramsey Crowe , who had been kept under house arrest , is escorted to the capital city of Randgriz in order to present evidence exonerating the weary soldiers and expose the real traitor , the Gallian General that had accused Kurt of Treason . 
 Partly due to these events , and partly due to the major losses in manpower Gallia suffers towards the end of the war with the Empire , the Nameless are offered a formal position as a squad in the Gallian Army rather than serve as an anonymous shadow force . This is short @-@ lived , however , as following Maximilian 's defeat , Dahau and Calamity Raven move to activate an ancient Valkyrian super weapon within the Empire , kept secret by their benefactor . Without the support of Maximilian or the chance to prove themselves in the war with Gallia , it is Dahau 's last trump card in creating a new Darcsen nation . As an armed Gallian force invading the Empire just following the two nations ' cease @-@ fire would certainly wreck their newfound peace , Kurt decides to once again make his squad the Nameless , asking Crowe to list himself and all under his command as killed @-@ in @-@ action . Now owing allegiance to none other than themselves , the 422nd confronts Dahau and destroys the Valkyrian weapon . Each member then goes their separate ways in order to begin their lives anew . 
 
 = = Development = = 
 
 Concept work for Valkyria Chronicles III began after development finished on Valkyria Chronicles II in early 2010 , with full development beginning shortly after this . The director of Valkyria Chronicles II , Takeshi Ozawa , returned to that role for Valkyria Chronicles III . Development work took approximately one year . After the release of Valkyria Chronicles II , the staff took a look at both the popular response for the game and what they wanted to do next for the series . Like its predecessor , Valkyria Chronicles III was developed for PlayStation Portable : this was due to the team wanting to refine the mechanics created for Valkyria Chronicles II , and they had not come up with the " revolutionary " idea that would warrant a new entry for the PlayStation 3 . Speaking in an interview , it was stated that the development team considered Valkyria Chronicles III to be the series ' first true sequel : while Valkyria Chronicles II had required a large amount of trial and error during development due to the platform move , the third game gave them a chance to improve upon the best parts of Valkyria Chronicles II due to being on the same platform . In addition to Sega staff from the previous games , development work was also handled by Media.Vision. The original scenario was written Kazuki Yamanobe , while the script was written by Hiroyuki Fujii , Koichi Majima , Kishiko Miyagi , Seiki Nagakawa and Takayuki Shouji . Its story was darker and more somber than that of its predecessor . 
 The majority of material created for previous games , such as the BLiTZ system and the design of maps , was carried over . Alongside this , improvements were made to the game 's graphics and some elements were expanded , such as map layouts , mission structure , and the number of playable units per mission . A part of this upgrade involved creating unique polygon models for each character 's body . In order to achieve this , the cooperative elements incorporated into the second game were removed , as they took up a large portion of memory space needed for the improvements . They also adjusted the difficulty settings and ease of play so they could appeal to new players while retaining the essential components of the series ' gameplay . The newer systems were decided upon early in development . The character designs were done by Raita Honjou , who had worked on the previous Valkyria Chronicles games . When creating the Nameless Squad , Honjou was faced with the same problem he had had during the first game : the military uniforms essentially destroyed character individuality , despite him needing to create unique characters the player could identify while maintaining a sense of reality within the Valkyria Chronicles world . The main color of the Nameless was black . As with the previous Valkyria games , Valkyria Chronicles III used the CANVAS graphics engine . The anime opening was produced by Production I.G. 
 
 = = = Music = = = 
 
 The music was composed by Hitoshi Sakimoto , who had also worked on the previous Valkyria Chronicles games . When he originally heard about the project , he thought it would be a light tone similar to other Valkyria Chronicles games , but found the themes much darker than expected . An early theme he designed around his original vision of the project was rejected . He redid the main theme about seven times through the music production due to this need to reassess the game . The main theme was initially recorded using orchestra , then Sakimoto removed elements such as the guitar and bass , then adjusted the theme using a synthesizer before redoing segments such as the guitar piece on their own before incorporating them into the theme . The rejected main theme was used as a hopeful tune that played during the game 's ending . The battle themes were designed around the concept of a " modern battle " divorced from a fantasy scenario by using modern musical instruments , constructed to create a sense of atonality . While Sakimoto was most used to working with synthesized music , he felt that he needed to incorporate live instruments such as orchestra and guitar . The guitar was played by Mitsuhiro Ohta , who also arranged several of the later tracks . The game 's opening theme song , " If You Wish for ... " ( もしも君が願うのなら , Moshimo Kimi ga Negauno Nara ) , was sung by Japanese singer May 'n . Its theme was the reason soldiers fought , in particular their wish to protect what was precious to them rather than a sense of responsibility or duty . Its lyrics were written by Seiko Fujibayashi , who had worked on May 'n on previous singles . 
 
 = = = Release = = = 
 
 In September 2010 , a teaser website was revealed by Sega , hinting at a new Valkyria Chronicles game . In its September issue , Famitsu listed that Senjō no Valkyria 3 would be arriving on the PlayStation Portable . Its first public appearance was at the 2010 Tokyo Game Show ( TGS ) , where a demo was made available for journalists and attendees . During the publicity , story details were kept scant so as not to spoil too much for potential players , along with some of its content still being in flux at the time of its reveal . To promote the game and detail the story leading into the game 's events , an episodic Flash visual novel written by Fujii began release in January 2011 . The game was released January 27 , 2011 . During an interview , the development team said that the game had the capacity for downloadable content ( DLC ) , but that no plans were finalized . Multiple DLC maps , featuring additional missions and recruitable characters , were released between February and April 2011 . An expanded edition of the game , Valkyria Chronicles III Extra Edition , released on November 23 , 2011 . Packaged and sold at a lower price than the original , Extra Edition game with seven additional episodes : three new , three chosen by staff from the game 's DLC , and one made available as a pre @-@ order bonus . People who also owned the original game could transfer their save data between versions . 
 Unlike its two predecessors , Valkyria Chronicles III was not released in the west . According to Sega , this was due to poor sales of Valkyria Chronicles II and the general unpopularity of the PSP in the west . An unofficial fan translation patch began development in February 2012 : players with a copy of Valkyria Chronicles III could download and apply the patch , which translated the game 's text into English . Compatible with the Extra Edition , the patch was released in January 2014 . 
 
 = = Reception = = 
 
 On its day of release in Japan , Valkyria Chronicles III topped both platform @-@ exclusive and multi @-@ platform sales charts . By early February , the game sold 102 @,@ 779 units , coming in second overall to The Last Story for the Wii . By the end of the year , the game had sold just over 152 @,@ 500 units . 
 Famitsu enjoyed the story , and were particularly pleased with the improvements to gameplay . Japanese gaming site Game Watch Impress , despite negatively noting its pacing and elements recycled from previous games , was generally positive about its story and characters , and found its gameplay entertaining despite off @-@ putting difficulty spikes . 4Gamer.net writer Naohiko Misuosame , in a " Play Test " article based on the game 's PSN demo , felt that Valkyria Chronicles III provided a " profound feeling of closure " for the Valkyria Chronicles series . He praised its gameplay despite annoying limitations to aspects such as special abilities , and positively noted its shift in story to a tone similar to the first game . 
 PlayStation Official Magazine - UK praised the story 's blurring of Gallia 's moral standing , art style , and most points about its gameplay , positively noting the latter for both its continued quality and the tweaks to balance and content . Its one major criticism were multiple difficulty spikes , something that had affected the previous games . Heath Hindman of gaming website PlayStation Lifestyle praised the addition of non @-@ linear elements and improvements or removal of mechanics from Valkyria Chronicles II in addition to praising the returning gameplay style of previous games . He also positively noted the story 's serious tone . Points criticized in the review were recycled elements , awkward cutscenes that seemed to include all characters in a scene for no good reason , pacing issues , and occasional problems with the game 's AI . 
 In a preview of the TGS demo , Ryan Geddes of IGN was left excited as to where the game would go after completing the demo , along with enjoying the improved visuals over Valkyria Chronicles II . Kotaku 's Richard Eisenbeis was highly positive about the game , citing is story as a return to form after Valkyria Chronicles II and its gameplay being the best in the series . His main criticisms were its length and gameplay repetition , along with expressing regret that it would not be localized . 
 
 = = Legacy = = 
 
 Kurt and Riela were featured in the Nintendo 3DS crossover Project X Zone , representing the Valkyria series . Media.Vision would return to the series to develop Valkyria : Azure Revolution , with Ozawa returning as director . Azure Revolution is a role @-@ playing video game for the PlayStation 4 that forms the beginning of a new series within the Valkyria franchise . 
 
 = = = Adaptations = = = 
 
 Valkyria Chronicles 3 was adapted into a two @-@ episode original video animation series in the same year of its release . Titled Senjō no Valkyria 3 : Taga Tame no Jūsō ( 戦場のヴァルキュリア３ 誰がための銃瘡 , lit . Valkyria of the Battlefield 3 : The Wound Taken for Someone 's Sake ) , it was originally released through PlayStation Network and Qriocity between April and May 2011 . The initially @-@ planned release and availability period needed to be extended due to a stoppage to PSN during the early summer of that year . It later released for DVD on June 29 and August 31 , 2011 , with separate " Black " and " Blue " editions being available for purchase . The anime is set during the latter half of Valkyria Chronicles III , detailing a mission by the Nameless against their Imperial rivals Calamity Raven . The anime was first announced in November 2010 . It was developed by A @-@ 1 Pictures , produced by Shinji Motoyama , directed by Nobuhiro Kondō , and written by Hiroshi Ōnogi . Sakimoto 's music for the game was used in the anime . 
 The anime 's title was inspired by the principle purpose of the Nameless : to suffer in battle for the goals of others . A subtitle attached to the project during development was " The Road to Kubinka " , which referenced the Kubinka Tank Museum in Moscow . The game 's main theme was how the characters regained their sense of self when stripped of their names and identities , along with general themes focused on war and its consequences . While making the anime , the production team were told by Sega to make it as realistic as possible , with the consequence that the team did extensive research into aspects such as what happened when vehicles like tanks were overturned or damaged . Due to it being along the same timeline as the original game and its television anime adaptation , the cast of Valkyria Chronicles could make appearances , which pleased the team . The opening theme , " Akari ( Light ) -Tomoshibi- " ( 灯 @-@ TOMOSHIBI- ) , was sung by Japanese singer Faylan . The ending theme , " Someday the Flowers of Light Will Bloom " ( いつか咲く光の花 , Itsuka Saku Hikari no Hana ) , was sung by Minami Kuribayashi . Both songs ' lyrics were written by their respective artists . 
 Two manga adaptations were produced , following each of the game 's main female protagonists Imca and Riela . They were Senjō no Valkyria 3 : Namo naki Chikai no Hana ( 戦場のヴァルキュリア3 名もなき誓いの花 , lit . Valkyria of the Battlefield 3 : The Flower of the Nameless Oath ) , illustrated by Naoyuki Fujisawa and eventually released in two volumes after being serialized in Dengeki Maoh between 2011 and 2012 ; and Senjō no Valkyria 3 : -Akaki Unmei no Ikusa Otome- ( 戦場のヴァルキュリア3 -赤き運命の戦乙女- , lit . Valkyria of the Battlefield 3 -The Valkyrie of the Crimson Fate ) , illustrated by Mizuki Tsuge and eventually released in a single volume by Kadokawa Shoten in 2012 . 
 
 
 = Tower Building of the Little Rock Arsenal = 
 
 The Tower Building of the Little Rock Arsenal , also known as U.S. Arsenal Building , is a building located in MacArthur Park in downtown Little Rock , Arkansas . Built in 1840 , it was part of Little Rock 's first military installation . Since its decommissioning , The Tower Building has housed two museums . It was home to the Arkansas Museum of Natural History and Antiquities from 1942 to 1997 and the MacArthur Museum of Arkansas Military History since 2001 . It has also been the headquarters of the Little Rock Æsthetic Club since 1894 . 
 The building receives its name from its distinct octagonal tower . Besides being the last remaining structure of the original Little Rock Arsenal and one of the oldest buildings in central Arkansas , it was also the birthplace of General Douglas MacArthur , who became the supreme commander of US forces in the South Pacific during World War II . It was also the starting place of the Camden Expedition . In 2011 it was named as one of the top 10 attractions in the state of Arkansas by Arkansas@. 
 
 = = Construction = = 
 
 The arsenal was constructed at the request of Governor James Sevier Conway in response to the perceived dangers of frontier life and fears of the many Native Americans who were passing through the state on their way to the newly established Oklahoma Territory . Thirty @-@ six acres were appropriated on the outskirts of Little Rock by Major Robert B. Lee of the U.S. Army . The land had been previously used as a racetrack by the local jockey club . John Wormley Walker , a builder for the Federal Government , supervised the construction . Originally $ 14 @,@ 000 was allocated for the construction of the arsenal , but proved inadequate . The budget was later increased to $ 30 @,@ 000 . Work began on the Tower Building in 1840 , and it was the first permanent structure of the arsenal to be built . Being originally constructed to store ammunition , the building was designed with 3 @-@ foot @-@ thick ( 0 @.@ 91 m ) exterior walls . The original plans called for it to be built of stone , however , masonry was used instead . The Arkansas Gazette referred to the structure as " A splendid specimen of masonry " . 
 
 = = Civil War = = 
 
 For several years the arsenal , which was owned by the federal government , served as a simple arms depot and was staffed with only a handful of soldiers . But in November 1860 , with the American Civil War on the horizon , a company of the Second United States Artillery , consisting of sixty @-@ five men , was transferred to Little Rock under the command of Captain James Totten . On January 15 , 1861 , the state legislature decided to hold a referendum to determine if a state convention should be held to consider the issue of secession and to elect delegates to such a convention . It was planned for February 18 ; however , events at the arsenal , would not wait . On January 28 , then Governor Henry Massey Rector informed Captain Totten that he and his soldiers would be " permitted to remain in the possession of the Federal officers until the State , by authority of the people , shall have determined to sever their connection with the General Government , " Totten responded to this by telling the Governor that his orders came from the United States Government and began a desperate but ultimately futile dispatch of letters and telegrams asking for reinforcements , although rumors were widely spread that they were already coming . The first telegraph wire to span between Little Rock and Memphis had recently been completed . Local attorney John M Harrel was asked to compose the first telegraph dispatched from Arkansas 's capital . In his message , Harrel reported unconfirmed rumors that more federal troops had been sent to reinforce the Little Rock Arsenal . 
 The United States troops at the outposts of the western frontier of the state and in the Indian nation have all been recalled from winter quarters to reinforce the garrison at Fort Smith . The garrison at Fort Smith had been previously transferred to the United States Arsenal in this city ( Little Rock ) . The arsenal is one of the richest depositories of military stores in the United States and is supposed to be the ultimate destination of the tropps [ sic ] ordered from the frontier . 
 -John M Harrel Telegram , January 31 , 1861 
 The item was intended simply as a piece of news , but telegraph lines quickly spread the news throughout the state , fueling procession sentiment . The rumor was interpreted by some Arkansans as a call from the governor to assemble to help expel the federal troops from the arsenal . By February 5 , six militia units , consisting of 1 @,@ 000 men , with a guarantee that the numbers could be increased to 5 @,@ 000 if the situations deemed it necessary , had assembled in Little Rock . Governor Rector vehemently denied ordering the troops to assemble or giving any order at all in connection with the troops . Faced with the fact that the military had assembled believing they were following his orders and the consensus of the citizens of Little Rock against any armed conflict between the civilian army and federal troops , Governor Rector was forced to take control of the situation . On February 6 , he sent a formal demand for surrender of the arsenal to Captain Totten , 
 This movement is prompted by the feeling that pervades the citizens of this State that in the present emergency the arms and munitions of war in the Arsenal should be under the control of the State authorities , in order to their security . This movement , although not authorized by me , has assumed such an aspect that it becomes my duty , as the executive of this Sate , to interpose my official authority to prevent a collision between the people of the State and the Federal troops under your command . I therefore demand in the name of the State the delivery of the possession of the Arsenal and munitions of war under your charge to the State authorities , to be held subject to the action of the convention to be held on the 4th of March next . 
 Perhaps because Abraham Lincoln had not yet been inaugurated as President , Captain Totten received no instructions from his superiors and was forced to withdraw his troops . He agreed to surrender the arsenal as long as the governor agreed to three provisions : 
 The governor would take possession of the arsenal in the name of the United States . 
 The soldiers would be allowed safe passage in any direction carrying any personal and public property besides munitions of war . 
 The soldiers would be allowed to march away as men leaving under orders , not as conquered and surrendering soldiers . 
 On the morning of February 8 , 1861 , Rector and Totten signed an agreement placing the arsenal in the hands of state officials . That afternoon , the citizen militia marched to the arsenal with Governor Rector at its head . All of the federal troops had left at this point , except Totten who had stayed behind to listen to the Governor 's speech and to hand the arsenal over in person . 
 The Little Rock Arsenal was classified in 1860 as an " arsenal of deposit , " meaning that it was simply a warehouse for the storage of weapons intended for the use of the state militia in times of crisis . Thus there were no substantial operations for ordnance fabrication or repairs , nor for the manufacture of cartridges at the time the Arsenal fell into State hands . Most of these operations were started from scratch through the efforts of the Arkansas Military Board . 
 Inside the Little Rock Arsenal after its seizure in February , 1861 , the Confederates inventoried some 10 @,@ 247 weapons , 250 @,@ 000 musket cartridges , and 520 @,@ 000 percussion caps , as well as the four bronze cannon of Totten 's battery . Long arms in the Arsenal 's inventory consisted of : 
 M1822 .69 cal ( flintlock ) 5 @,@ 625 
 M1822 .69 cal ( percussion @-@ converted ) 53 
 M1842 .69 cal smoothbore ( percussion ) 357 
 M1855 .58 cal rifle @-@ muskets 900 
 M1817 common rifles 125 
 M1841 rifle ( " Mississippi Rifle " ) 54 
 M1847 musketoon 2 
 Hall 's carbines 267 
 Hall 's rifles ( flintlock ) 2 @,@ 864 
 Total 10 @,@ 247 '''))

