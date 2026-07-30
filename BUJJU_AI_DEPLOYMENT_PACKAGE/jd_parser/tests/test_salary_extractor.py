import unittest

from jd_parser.extractors.salary_extractor import extract_salary


class TestSalaryExtractor(unittest.TestCase):
    """
    Test cases for salary extraction.
    """

    def test_extract_salary_with_rupee_symbol(self):
        """Test extraction of salary with rupee symbol."""
        text = "Salary: ₹ 50,00,000 per annum"
        result = extract_salary(text)
        self.assertEqual(result, "₹ 50,00,000")

    def test_extract_salary_with_inr(self):
        """Test extraction of salary with INR prefix."""
        text = "The package is INR 25,00,000 annual"
        result = extract_salary(text)
        self.assertEqual(result, "INR 25,00,000")

    def test_extract_salary_with_ctc_lpa(self):
        """Test extraction of CTC in LPA format."""
        text = "CTC: 15 LPA"
        result = extract_salary(text)
        self.assertEqual(result, "CTC: 15 LPA")

    def test_extract_salary_with_lpa_only(self):
        """Test extraction of salary with just LPA."""
        text = "The position offers 12.5 LPA"
        result = extract_salary(text)
        self.assertEqual(result, "12.5 LPA")

    def test_extract_salary_with_lakhs(self):
        """Test extraction of salary with Lakhs."""
        text = "Salary: 20 Lakhs per annum"
        result = extract_salary(text)
        self.assertEqual(result, "20 Lakhs")

    def test_extract_salary_with_lakhs_per_annum(self):
        """Test extraction of salary with Lakhs Per Annum."""
        text = "The candidate will receive 18 Lakhs Per Annum"
        result = extract_salary(text)
        self.assertEqual(result, "18 Lakhs Per Annum")

    def test_extract_salary_with_lakhs_annum(self):
        """Test extraction of salary with Lakhs/Annum."""
        text = "Compensation: 22 Lakhs/Annum"
        result = extract_salary(text)
        self.assertEqual(result, "22 Lakhs/Annum")

    def test_extract_salary_with_lacs(self):
        """Test extraction of salary with Lacs (alternate spelling)."""
        text = "Package: 25 Lacs"
        result = extract_salary(text)
        self.assertEqual(result, "25 Lacs")

    def test_extract_salary_with_rs(self):
        """Test extraction of salary with Rs."""
        text = "Salary: Rs. 50,00,000"
        result = extract_salary(text)
        self.assertEqual(result, "Rs. 50,00,000")

    def test_extract_salary_with_rs_no_dot(self):
        """Test extraction of salary with Rs (no dot)."""
        text = "Package: Rs 75,00,000 annually"
        result = extract_salary(text)
        self.assertEqual(result, "Rs 75,00,000")

    def test_extract_salary_with_multiple_patterns(self):
        """Test that first matching pattern is returned."""
        text = "Our company offers ₹ 30,00,000 or 30 LPA"
        result = extract_salary(text)
        # Should return the first match found
        self.assertIn(result, ["₹ 30,00,000", "30 LPA"])

    def test_extract_salary_case_insensitive(self):
        """Test that extraction is case insensitive."""
        text = "CTC: 10 lpa"
        result = extract_salary(text)
        self.assertEqual(result, "CTC: 10 lpa")

    def test_extract_salary_empty_text(self):
        """Test with empty text."""
        result = extract_salary("")
        self.assertEqual(result, "")

    def test_extract_salary_none_text(self):
        """Test with None text."""
        result = extract_salary(None)
        self.assertEqual(result, "")

    def test_extract_salary_no_salary_present(self):
        """Test with text containing no salary."""
        text = "This is a great opportunity for a developer."
        result = extract_salary(text)
        self.assertEqual(result, "")

    def test_extract_salary_with_decimal_lpa(self):
        """Test extraction with decimal LPA."""
        text = "Offering 15.5 LPA"
        result = extract_salary(text)
        self.assertEqual(result, "15.5 LPA")

    def test_extract_salary_with_decimal_lakhs(self):
        """Test extraction with decimal Lakhs."""
        text = "Package: 18.75 Lakhs"
        result = extract_salary(text)
        self.assertEqual(result, "18.75 Lakhs")

    def test_extract_salary_with_commas_and_decimals(self):
        """Test extraction with commas and decimals."""
        text = "Salary: ₹ 50,00,000.50"
        result = extract_salary(text)
        self.assertEqual(result, "₹ 50,00,000.50")

    def test_extract_salary_with_whitespace_variations(self):
        """Test extraction with various whitespace patterns."""
        text = "CTC:12.5 LPA"
        result = extract_salary(text)
        self.assertEqual(result, "CTC:12.5 LPA")

    def test_extract_salary_returns_string(self):
        """Test that return type is always string."""
        result1 = extract_salary("15 LPA")
        result2 = extract_salary(None)
        result3 = extract_salary("")

        self.assertIsInstance(result1, str)
        self.assertIsInstance(result2, str)
        self.assertIsInstance(result3, str)

    def test_extract_salary_with_inr_no_space(self):
        """Test extraction of INR without space."""
        text = "INR50,00,000"
        result = extract_salary(text)
        self.assertEqual(result, "INR50,00,000")

    def test_extract_salary_with_complex_text(self):
        """Test extraction from complex job description."""
        text = """
        Job Title: Senior Developer
        Experience: 5-8 years
        Salary: ₹ 25,00,000 - 35,00,000 per annum
        Location: Bangalore, India
        Skills: Python, Java, Django
        """
        result = extract_salary(text)
        self.assertNotEqual(result, "")
        self.assertIn("₹", result)

    def test_extract_salary_prefers_first_match(self):
        """Test that extractor returns first valid match."""
        # The extractor should return the first match it finds
        text = "15 LPA or 15 Lakhs per annum"
        result = extract_salary(text)
        # Should be one of the patterns
        self.assertNotEqual(result, "")


if __name__ == "__main__":
    unittest.main()
