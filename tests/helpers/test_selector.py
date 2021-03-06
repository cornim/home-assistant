"""Test selectors."""
import pytest
import voluptuous as vol

from homeassistant.helpers import selector


@pytest.mark.parametrize(
    "schema",
    (
        {"device": None},
        {"entity": None},
    ),
)
def test_valid_base_schema(schema):
    """Test base schema validation."""
    selector.validate_selector(schema)


@pytest.mark.parametrize(
    "schema",
    (
        {},
        {"non_existing": {}},
        # Two keys
        {"device": {}, "entity": {}},
    ),
)
def test_invalid_base_schema(schema):
    """Test base schema validation."""
    with pytest.raises(vol.Invalid):
        selector.validate_selector(schema)


def test_validate_selector():
    """Test return is the same as input."""
    schema = {"device": {"manufacturer": "mock-manuf", "model": "mock-model"}}
    assert schema == selector.validate_selector(schema)


@pytest.mark.parametrize(
    "schema",
    (
        {},
        {"integration": "zha"},
        {"manufacturer": "mock-manuf"},
        {"model": "mock-model"},
        {"manufacturer": "mock-manuf", "model": "mock-model"},
        {"integration": "zha", "manufacturer": "mock-manuf", "model": "mock-model"},
        {"entity": {"device_class": "motion"}},
        {
            "integration": "zha",
            "manufacturer": "mock-manuf",
            "model": "mock-model",
            "entity": {"domain": "binary_sensor", "device_class": "motion"},
        },
    ),
)
def test_device_selector_schema(schema):
    """Test device selector."""
    selector.validate_selector({"device": schema})


@pytest.mark.parametrize(
    "schema",
    (
        {},
        {"integration": "zha"},
        {"domain": "light"},
        {"device_class": "motion"},
        {"integration": "zha", "domain": "light"},
        {"integration": "zha", "domain": "binary_sensor", "device_class": "motion"},
    ),
)
def test_entity_selector_schema(schema):
    """Test entity selector."""
    selector.validate_selector({"entity": schema})


@pytest.mark.parametrize(
    "schema",
    ({},),
)
def test_area_selector_schema(schema):
    """Test area selector."""
    selector.validate_selector({"area": schema})


@pytest.mark.parametrize(
    "schema",
    (
        {"min": 10, "max": 50},
        {"min": -100, "max": 100, "step": 5},
        {"min": -20, "max": -10, "mode": "box"},
        {"min": 0, "max": 100, "unit_of_measurement": "seconds", "mode": "slider"},
        {"min": 10, "max": 1000, "mode": "slider", "step": 0.5},
    ),
)
def test_number_selector_schema(schema):
    """Test number selector."""
    selector.validate_selector({"number": schema})


@pytest.mark.parametrize(
    "schema",
    ({},),
)
def test_boolean_selector_schema(schema):
    """Test boolean selector."""
    selector.validate_selector({"boolean": schema})


@pytest.mark.parametrize(
    "schema",
    ({},),
)
def test_time_selector_schema(schema):
    """Test time selector."""
    selector.validate_selector({"time": schema})
