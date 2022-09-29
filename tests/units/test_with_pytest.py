from backend.app import Skill

def test_new_skill():
    """
    GIVEN a Skill model
    WHEN a new Skill is created
    THEN check the skil_id, skill_name, skill_status are defined correctly
    """
    skill = Skill(1, 'patkennedy79@gmail.com',1)
    assert skill.skill_id == 1
    assert skill.skill_name == 'patkennedy79@gmail.com'
    assert skill.skill_status == 1