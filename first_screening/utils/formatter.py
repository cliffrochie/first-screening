import re


def format_topic(topic: object) -> dict:
    formatted_topic = {}
    formatted_topic["id"] = topic.id
    formatted_topic["name_id"] = topic.name_id
    formatted_topic["name"] = topic.name
    formatted_topic["description"] = topic.description
    
    return formatted_topic


def format_content(content: object) -> dict:
    formatted_content = {}
    formatted_content["id"] = content.id
    formatted_content["sequence_number"] = content.sequence_number
    formatted_content["title"] = content.title
    formatted_content["body"] = content.body
    formatted_content["topic_id"] = content.topic_id

    return formatted_content


def format_name_id(name: str) -> str:
    result = re.sub(r"[^A-Za-z0-9]+", " ", name)
    return result.lower().strip().replace(" ", "-")
