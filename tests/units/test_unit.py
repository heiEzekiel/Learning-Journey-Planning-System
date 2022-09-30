from backend.app import JobRole
import pytest 

#----------- test_job_role ------------------
def test_create_job_role_success():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created
    THEN check the job_role_name, job_role_desc, job_role_status are defined correctly
    """
    test_job_role = JobRole('Human Resource', 'HR', 0)
    assert test_job_role.job_role_name == 'Human Resource'
    assert test_job_role.job_role_desc == 'HR'
    assert test_job_role.job_role_status == 0

def test_create_job_role_invalid_name():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_name
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole(123, 'HR', 0)

def test_create_job_role_invalid_desc():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_desc
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole('Human Resource', 123, 0)

def test_create_job_role_invalid_status():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_status
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole('Human Resource', 'HR', '0')\

def test_create_job_role_invalid_parameters():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with invalid amount of parameters
    THEN check the TypeError is raised
    """
    with pytest.raises(Exception):
        JobRole(0, 'Human Resource', 'HR', 0)
