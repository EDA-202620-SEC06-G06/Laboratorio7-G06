from datetime import date

import pytest

from App import logic
from App import view


def add_crime(analyzer, occurred_on, offense):
    logic.add_crime(
        analyzer,
        {
            "OCCURRED_ON_DATE": occurred_on,
            "OFFENSE_CODE_GROUP": offense,
        },
    )


def test_index_queries_on_empty_analyzer():
    analyzer = logic.new_logic()

    assert logic.index_height(analyzer) == 0
    assert logic.index_size(analyzer) == 0
    assert logic.min_key(analyzer) is None
    assert logic.max_key(analyzer) is None
    assert logic.get_crimes_by_range(analyzer, "2024-02-01", "2024-02-03") == 0
    assert logic.get_crimes_by_range_code(analyzer, "2024-02-01", "A") == 0


def test_date_range_and_offense_queries():
    analyzer = logic.new_logic()
    add_crime(analyzer, "2024-02-02 10:00:00", "A")
    add_crime(analyzer, "2024-02-01 12:00:00", "B")
    add_crime(analyzer, "2024-02-02 18:00:00", "A")
    add_crime(analyzer, "2024-02-03 09:00:00", "C")

    assert logic.index_size(analyzer) == 3
    assert logic.min_key(analyzer) == date(2024, 2, 1)
    assert logic.max_key(analyzer) == date(2024, 2, 3)
    assert logic.get_crimes_by_range(analyzer, "2024-02-01", "2024-02-02") == 3
    assert logic.get_crimes_by_range(analyzer, date(2024, 2, 2), date(2024, 2, 2)) == 2
    assert logic.get_crimes_by_range_code(analyzer, "2024-02-02", "A") == 2
    assert logic.get_crimes_by_range_code(analyzer, "2024-02-02", "B") == 0
    assert logic.get_crimes_by_range_code(analyzer, "2024-02-04", "A") == 0
    assert logic.get_crimes_by_range(analyzer, "2024-02-04", "2024-02-01") == 0


def test_menu_range_and_offense_queries(monkeypatch, capsys):
    inputs = iter(
        (
            "1",
            "2",
            "3",
            "2024-02-01",
            "2024-02-02",
            "4",
            "2024-02-02",
            "A",
            "0",
        )
    )
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(inputs))

    def load_sample_data(analyzer, _crimefile):
        add_crime(analyzer, "2024-02-02 10:00:00", "A")
        add_crime(analyzer, "2024-02-01 12:00:00", "B")
        add_crime(analyzer, "2024-02-02 18:00:00", "A")
        return analyzer

    monkeypatch.setattr(view.logic, "load_data", load_sample_data)

    with pytest.raises(SystemExit) as exit_info:
        view.main()

    output = capsys.readouterr().out
    assert exit_info.value.code == 0
    assert "Total de crimenes en el rango de fechas: 3" in output
    assert "Total de ofensas tipo: A en esa fecha:  2" in output
