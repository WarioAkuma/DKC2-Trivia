import orjson
import pkgutil
from typing import List, Dict
from .parser import parser_version_1, parser_version_2
from .types import Topic

short_game_names = {
    "A Link to the Past": "TLoZ: ALttP",
    "Castlevania - Circle of the Moon": "CV: CotM",
    "Diddy Kong Racing": "DKR",
    "Donkey Kong Country": "DKC",
    "Donkey Kong Country 2": "DKC2",
    "Donkey Kong Country 3": "DKC3",
    "Final Fantasy Mystic Quest": "FFMQ",
    "Kingdom Hearts": "KH1",
    "Kingdom Hearts 2": "KH2",
    "Kirby 64 - The Crystal Shards": "K64",
    "Kirby Super Star": "KSS",
    "Kirby's Dream Land 3": "KDL3",
    "Mario & Luigi Superstar Saga": "MLSS",
    "Mario Kart Double Dash": "MKDD",
    "Paper Mario": "PM64",
    "Paper Mario: The Thousand-Year Door": "TTYD",
    "Pokemon Crystal": "PKMN: Crystal",
    "Pokemon Emerald": "PKMN: Emerald",
    "Pokemon FireRed and LeafGreen": "PKMN: FRLG",
    "Pokemon Red and Blue": "PKMN: RB",
    "Skyward Sword": "TLoZ: SS",
    "Sonic Adventure 2 Battle": "SA2B",
    "Super Mario World": "SMW",
    "Super Mario Sunshine": "SMS",
    "Symphony of the Night": "CV: SotN",
    "The Binding of Isaac Repentance": "TBoIR",
    "The Legend of Zelda": "TLoZ",
    "Zelda II: The Adventure of Link": "Zelda II",
    "Twilight Princess": "TLoZ: TP",
    "The Wind Waker": "TLoZ: WW",
    "Links Awakening DX": "LADX",
    "The Legend of Zelda - Oracle of Seasons": "TLoZ: OoS",
    "The Legend of Zelda - Oracle of Ages": "TLoZ: OoA",
    "The Minish Cap": "TLoZ: TMC",
    "A Link Between Worlds": "TLoZ: ALBW",
    "Majora's Mask Recompiled": "TLoZ: MM",
    "Ocarina of Time": "TLoZ: OoT",
    "Metroid Zero Mission": "Metroid ZM",
    "Castlevania - Harmony of Dissonance": "CV: HoD",
    "Castlevania: Dawn of Sorrow": "CV: DoS",
    "Final Fantasy IV Free Enterprise": "FF4",
    "Final Fantasy 6 Worlds Collide": "FF6",
    "Golden Sun The Lost Age": "Golden Sun",
    "Super Mario Land 2": "SML2",
    "Sonic Adventure DX": "SADX",
    "The Simpsons Hit And Run": "SHAR",
    "Momodora Moonlit Farewell": "Momodora 5",
    "Yoku's Island Express": "Yoku's Island",
    "Plants vs. Zombies: Replanted": "PvZ: Replanted",
}

shorter_game_names = {
}


game_aliases = {
    "Celeste (Open World)": "Celeste",
    "Ship of Harkinian": "Ocarina of Time",
    "SMW: Spicy Mycena Waffles": "Super Mario World",
    "yrtnuoC gnoK yeknoD": "Donkey Kong Country",
}


def parse_single_topic(topic_data: List[str], is_dkc2: bool) -> Topic | None:
    if "PARSER:" not in topic_data[0]:
        print (f"Failed to fetch the game name.")
        return None
    parser_version = int(topic_data[0].split(": ")[1].rstrip())
    if parser_version == 1:
        return parser_version_1(topic_data, is_dkc2)
    elif parser_version == 2:
        return parser_version_2(topic_data, is_dkc2)
    else:
        print (f"Invalid or non supported parser version.")
        return None


def parse_topics(is_dkc2: bool = False) -> Dict[str, Topic]:
    trivia_topics: Dict[str, Topic] = {}

    data = pkgutil.get_data(__name__, f"data/topics.json").decode("utf-8")
    topic_index = orjson.loads(data)

    for topic_path in topic_index:
        topic_data = pkgutil.get_data(__name__, f"{topic_path}").decode("utf-8")
        parsed_topic = parse_single_topic(topic_data.splitlines(), is_dkc2)
        if parsed_topic is None:
            continue
        topic_name = parsed_topic.topic_name
        if topic_name not in trivia_topics.keys():
            trivia_topics[topic_name] = parsed_topic
        else:
            trivia_topics[topic_name].easy_questions += parsed_topic.easy_questions
            trivia_topics[topic_name].medium_questions += parsed_topic.medium_questions
            trivia_topics[topic_name].hard_questions += parsed_topic.hard_questions

    #trivia = trivia_topics["Ocarina of Time"]
    #for question_data in trivia.easy_questions:
    #    print (question_data.question, " | ", question_data.correct_answer, " | ", question_data.incorrect_answer_1, " | ", question_data.incorrect_answer_2)

    return trivia_topics
