# backend/app/nlp/__init__.py

from .keywords import extract_keywords
from .topic_classifier import classify_topic
from .novelty import novelty_score
from .citation import extract_citations
from .gap_detector import gap_summary
from .section_graph import build_section_graph, graph_to_dict
