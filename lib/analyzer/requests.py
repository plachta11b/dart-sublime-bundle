"""Requests for the anlyzer server.
"""

def set_roots(id_, included=[], excluded=[]):
    return {"id": id_,
        "method": "analysis.setAnalysisRoots",
        "params": {
            "included": included,
            "excluded": excluded
            }
        }


def set_priority_files(id_, files=[]):
    return {"id": id_,
        "method": "analysis.setPriorityFiles",
        "params": {
            "files": files
            }
        }


def find_top_level_decls(id_, pattern):
    return {
      "id": id_,
      "method": "search.findTopLevelDeclarations",
      "params": {
        "pattern": pattern
      }
    }


def update_content(id_, files={}):
    return {
      "id": id_,
      "method": "analysis.updateContent",
      "params": {
        "files": files
      }
    }
