import pytest
from audio import footstep_surface as mod

CASES = [
    ("material_metal", "m.material_for('metal') == 'metal'"),
    ("material_unknown", "m.material_for('unknown') == 'default'"),
    ("frequency_double", "m.step_frequency(2.0, 1.0) == approx(2.0)"),
    ("landing_true", "m.landing_height(0.2, 0.3) is True"),
    ("landing_false", "m.landing_height(0.5, 0.3) is False"),
    ("event_run", "m.event_for('run') == 'run'"),
    ("event_jump", "m.event_for('jump') == 'jump'"),
    ("group_three", "m.group_footsteps(3) == 3"),
    ("delay_half", "m.fixed_delay(480, 48000) == approx(0.01)"),
    ("indoor_label", "m.indoor_reverb(True) == 'indoor'"),
    ("outdoor_label", "m.indoor_reverb(False) == 'outdoor'"),
    ("sync_diff", "m.sync_to_animation(0.5, 0.3) == approx(0.2)"),
    ("gain_near", "m.distance_gain(0.0, 10.0) == approx(1.0)"),
    ("gain_far", "m.distance_gain(10.0, 10.0) == approx(0.0)"),
    ("underwater_swap", "m.underwater_material(True, 'wood') == 'underwater'")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
