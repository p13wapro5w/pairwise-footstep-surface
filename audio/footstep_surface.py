"""第 55 批：角色在金属、草地、木板上脚步声一样、跑跳切换没声..."""

def material_for(tag):
    """按地形标签返回脚步材质。"""
    raise NotImplementedError("TODO: material_for")

def step_frequency(speed, base_frequency):
    """按速度返回步频。"""
    raise NotImplementedError("TODO: step_frequency")

def landing_height(height, threshold):
    """判断是否达到落地阈值。"""
    raise NotImplementedError("TODO: landing_height")

def event_for(mode):
    """按走跑跳返回脚步事件。"""
    raise NotImplementedError("TODO: event_for")

def group_footsteps(count):
    """返回多人脚步分组数。"""
    raise NotImplementedError("TODO: group_footsteps")

def fixed_delay(buffer_size, sample_rate):
    """返回固定脚步延迟。"""
    raise NotImplementedError("TODO: fixed_delay")

def indoor_reverb(is_indoor):
    """返回室内外混响组。"""
    raise NotImplementedError("TODO: indoor_reverb")

def sync_to_animation(event_time, animation_time):
    """返回脚步与动画时间差。"""
    raise NotImplementedError("TODO: sync_to_animation")

def distance_gain(distance, max_distance):
    """按距离返回脚步音量。"""
    raise NotImplementedError("TODO: distance_gain")

def underwater_material(is_underwater, material):
    """水下脚步材质。"""
    raise NotImplementedError("TODO: underwater_material")
