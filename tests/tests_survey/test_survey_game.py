from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_game):
    if survey_utils.get_category_from_survey(survey_game) != "jeuxvideo":
        raise AssertionError()


def test_get_rows_from_survey(survey_game):
    rows = survey_utils.get_rows_from_survey(survey_game)
    if len(rows) != 10:
        print(len(rows))
        raise AssertionError()


def test_get_infos_from_survey(survey_game):
    category = survey_utils.get_category_from_survey(survey_game)

    infos = survey_utils.get_survey_infos(survey_game, category)

    if len(infos) != 10:
        raise AssertionError()

    if infos[0]["Title"] != "Les Sims":
        raise AssertionError()
