# https://github.com/stopwords-iso/stopwords-cs/blob/master/stopwords-cs.json
class StopwordsRemover():

    def __init__(self):
        self.stopwords = [
            "a","aby","ahoj","aj","ale","anebo","ani","aniž","ano","asi","aspoň","atd","atp","az","ačkoli","až","bez",
            "beze","blízko","bohužel","brzo","bude","budem","budeme","budes","budete","budeš","budou","budu","by","byl",
            "byla","byli","bylo","byly","bys","byt","být","během","chce","chceme","chcete","chceš","chci","chtít","chtějí",
            "chut'","chuti","ci","clanek","clanku","clanky","co","coz","což","cz","daleko","dalsi","další","den","deset",
            "design","devatenáct","devět","dnes","do","dobrý","docela","dva","dvacet","dvanáct","dvě","dál","dále","děkovat",
            "děkujeme","děkuji","email","ho","hodně","i","jak","jakmile","jako","jakož","jde","je","jeden","jedenáct","jedna",
            "jedno","jednou","jedou","jeho","jehož","jej","jeji","jejich","její","jelikož","jemu","jen","jenom","jenž","jeste",
            "jestli","jestliže","ještě","jež","ji","jich","jimi","jinak","jine","jiné","jiz","již","jsem","jses","jseš","jsi",
            "jsme","jsou","jste","já","jí","jím","jíž","jšte","k","kam","každý","kde","kdo","kdy","kdyz","když","ke","kolik","kromě",
            "ktera","ktere","kteri","kterou","ktery","která","které","který","kteři","kteří","ku","kvůli","ma","mají","mate","me","mezi",
            "mi","mit","mne","mnou","mně","moc","mohl","mohou","moje","moji","možná","muj","musí","muze","my","má","málo","mám","máme",
            "máte","máš","mé","mí","mít","mě","můj","může","na","nad","nade","nam","napiste","napište","naproti","nas","nasi","načež",
            "naše","naši","ne","nebo","nebyl","nebyla","nebyli","nebyly","nechť","nedělají","nedělá","nedělám","neděláme","neděláte",
            "neděláš","neg","nejsi","nejsou","nemají","nemáme","nemáte","neměl","neni","není","nestačí","nevadí","nez","než","nic","nich",
            "nimi","nove","novy","nové","nový","nula","ná","nám","námi","nás","náš","ní","ním","ně","něco","nějak","někde","někdo","němu",
            "němuž","o","od","ode","on","ona","oni","ono","ony","osm","osmnáct","pak","patnáct","po","pod","podle","pokud","potom","pouze",
            "pozdě","pořád","prave","pravé","pred","pres","pri","pro","proc","prostě","prosím","proti","proto","protoze","protože","proč",
            "prvni","první","práve","pta","pět","před","přede","přes","přese","při","přičemž","re","rovně","s","se","sedm","sedmnáct","si",
            "sice","skoro","smí","smějí","snad","spolu","sta","sto","strana","sté","sve","svych","svym","svymi","své","svých","svým","svými",
            "svůj","ta","tady","tak","take","takhle","taky","takze","také","takže","tam","tamhle","tamhleto","tamto","tato","te","tebe","tebou",
            "ted'","tedy","tema","ten","tento","teto","ti","tim","timto","tipy","tisíc","tisíce","to","tobě","tohle","toho","tohoto","tom","tomto",
            "tomu","tomuto","toto","trošku","tu","tuto","tvoje","tvá","tvé","tvůj","ty","tyto","téma","této","tím","tímto","tě","těm","těma","těmu",
            "třeba","tři","třináct","u","určitě","uz","už","v","vam","vas","vase","vaše","vaši","ve","vedle","večer","vice","vlastně","vsak","vy","vám",
            "vámi","vás","váš","více","však","všechen","všechno","všichni","vůbec","vždy","z","za","zatímco","zač","zda","zde","ze","zpet","zpravy","zprávy",
            "zpět","čau","či","článek","článku","články","čtrnáct","čtyři","šest","šestnáct","že",
            # added by author
            " ", "který", "člověk", "mít", "muset", "všechen", "on", "ona", "ono", "ten", "ta", "to", "dít", "člověk", "procento", "velmi", "foto",
            # should have been added, but wasn't
            "říci", "uvést", "moci" 
        ]

        self.stopwords = frozenset(self.stopwords)

    def remove_stopwords(self, sentence_vec):
        newsentece = []

        for token in sentence_vec:
            if not token.lower() in self.stopwords:
                newsentece.append(token)

        return newsentece

    def is_stopword(self, token):
        return token.lower() in self.stopwords