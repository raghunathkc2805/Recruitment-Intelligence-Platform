import unittest

from jd_parser.extractors.employment_type_extractor import extract_employment_type


class TestEmploymentTypeExtractor(unittest.TestCase):
    """
    Test cases for employment type and work mode extraction.
    """

    # Employment Type Tests

    def test_extract_employment_type_full_time(self):
        """Test extraction of Full Time employment type."""
        text = "This is a Full Time position"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Full Time")
        self.assertEqual(result["work_mode"], "")

    def test_extract_employment_type_full_time_hyphenated(self):
        """Test extraction of Full-Time employment type."""
        text = "We are hiring for a full-time role"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Full Time")

    def test_extract_employment_type_permanent(self):
        """Test extraction of Permanent employment type."""
        text = "Permanent position available"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Permanent")

    def test_extract_employment_type_contract(self):
        """Test extraction of Contract employment type."""
        text = "Contract based job"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Contract")

    def test_extract_employment_type_contract_to_hire(self):
        """Test extraction of Contract to Hire employment type."""
        text = "Contract to Hire opportunity available"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Contract to Hire")

    def test_extract_employment_type_c2h_alias(self):
        """Test extraction of C2H (Contract to Hire alias)."""
        text = "Position available as C2H"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Contract to Hire")

    def test_extract_employment_type_freelance(self):
        """Test extraction of Freelance employment type."""
        text = "Freelance work available"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Freelance")

    def test_extract_employment_type_freelancer(self):
        """Test extraction of Freelancer employment type."""
        text = "Looking for a freelancer"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Freelance")

    def test_extract_employment_type_internship(self):
        """Test extraction of Internship employment type."""
        text = "Summer Internship position"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Internship")

    def test_extract_employment_type_intern(self):
        """Test extraction of Intern employment type."""
        text = "We hire interns for this role"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Internship")

    def test_extract_employment_type_apprenticeship(self):
        """Test extraction of Apprenticeship employment type."""
        text = "Apprenticeship program available"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Apprenticeship")

    def test_extract_employment_type_apprentice(self):
        """Test extraction of Apprentice employment type."""
        text = "We need an apprentice for training"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Apprenticeship")

    def test_extract_employment_type_temporary(self):
        """Test extraction of Temporary employment type."""
        text = "Temporary position for 3 months"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Temporary")

    def test_extract_employment_type_temp(self):
        """Test extraction of Temp employment type."""
        text = "We have a temp role available"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Temporary")

    def test_extract_employment_type_part_time(self):
        """Test extraction of Part Time employment type."""
        text = "Part Time opportunities available"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Part Time")

    def test_extract_employment_type_part_time_hyphenated(self):
        """Test extraction of Part-Time employment type."""
        text = "Looking for part-time staff"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Part Time")

    # Work Mode Tests

    def test_extract_work_mode_remote(self):
        """Test extraction of Remote work mode."""
        text = "This is a remote position"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Remote")

    def test_extract_work_mode_hybrid(self):
        """Test extraction of Hybrid work mode."""
        text = "Hybrid work model preferred"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Hybrid")

    def test_extract_work_mode_onsite(self):
        """Test extraction of Onsite work mode."""
        text = "Onsite position in Bangalore"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Onsite")

    def test_extract_work_mode_work_from_home(self):
        """Test extraction of Work From Home work mode."""
        text = "Work from home allowed"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Remote")

    def test_extract_work_mode_wfh_alias(self):
        """Test extraction of WFH (Work From Home alias)."""
        text = "Position available as WFH"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Remote")

    def test_extract_work_mode_office_based(self):
        """Test extraction of Office Based work mode."""
        text = "Office based work required"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Onsite")

    def test_extract_work_mode_work_from_office(self):
        """Test extraction of Work From Office work mode."""
        text = "Work from office 5 days a week"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Onsite")

    def test_extract_work_mode_wfo_alias(self):
        """Test extraction of WFO (Work From Office alias)."""
        text = "WFO model, located in Pune"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Onsite")

    # Combined Tests

    def test_extract_both_employment_and_work_mode(self):
        """Test extraction of both employment type and work mode."""
        text = "Full Time Remote position available"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Full Time")
        self.assertEqual(result["work_mode"], "Remote")

    def test_extract_permanent_hybrid(self):
        """Test extraction of Permanent + Hybrid."""
        text = "Permanent Hybrid role"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Permanent")
        self.assertEqual(result["work_mode"], "Hybrid")

    def test_extract_contract_onsite(self):
        """Test extraction of Contract + Onsite."""
        text = "Contract position, onsite only"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Contract")
        self.assertEqual(result["work_mode"], "Onsite")

    # Case Insensitivity Tests

    def test_extract_employment_type_case_insensitive_lowercase(self):
        """Test case insensitivity with lowercase."""
        text = "full time position"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Full Time")

    def test_extract_employment_type_case_insensitive_uppercase(self):
        """Test case insensitivity with uppercase."""
        text = "FULL TIME POSITION"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Full Time")

    def test_extract_work_mode_case_insensitive(self):
        """Test work mode case insensitivity."""
        text = "REMOTE work available"
        result = extract_employment_type(text)
        self.assertEqual(result["work_mode"], "Remote")

    # Edge Cases

    def test_extract_employment_type_empty_text(self):
        """Test with empty text."""
        result = extract_employment_type("")
        self.assertEqual(result["employment_type"], "")
        self.assertEqual(result["work_mode"], "")

    def test_extract_employment_type_none_text(self):
        """Test with None text."""
        result = extract_employment_type(None)
        self.assertEqual(result["employment_type"], "")
        self.assertEqual(result["work_mode"], "")

    def test_extract_employment_type_no_match(self):
        """Test with text containing no employment type."""
        text = "This is a great opportunity for a developer."
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "")
        self.assertEqual(result["work_mode"], "")

    # Complex Text Tests

    def test_extract_from_complex_jd(self):
        """Test extraction from complex job description."""
        text = """
        Job Title: Senior Developer
        Employment Type: Full Time
        Location: Remote
        We are looking for a full time remote developer.
        """
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Full Time")
        self.assertEqual(result["work_mode"], "Remote")

    def test_extract_return_type_is_dict(self):
        """Test that return type is always a dict."""
        result = extract_employment_type("Full Time")
        self.assertIsInstance(result, dict)
        self.assertIn("employment_type", result)
        self.assertIn("work_mode", result)

    def test_extract_dict_values_are_strings(self):
        """Test that dictionary values are always strings."""
        result1 = extract_employment_type("Full Time")
        result2 = extract_employment_type(None)
        result3 = extract_employment_type("")

        self.assertIsInstance(result1["employment_type"], str)
        self.assertIsInstance(result1["work_mode"], str)
        self.assertIsInstance(result2["employment_type"], str)
        self.assertIsInstance(result2["work_mode"], str)
        self.assertIsInstance(result3["employment_type"], str)
        self.assertIsInstance(result3["work_mode"], str)

    def test_extract_contractual(self):
        """Test extraction of Contractual employment type."""
        text = "Contractual position"
        result = extract_employment_type(text)
        self.assertEqual(result["employment_type"], "Contract")

    def test_extract_first_match_priority(self):
        """Test that first matching employment type is returned."""
        text = "Full Time and Part Time opportunities"
        result = extract_employment_type(text)
        self.assertIn(result["employment_type"], ["Full Time", "Part Time"])


if __name__ == "__main__":
    unittest.main()
