from pathlib import Path

p = Path("api/services/jd_service.py")
t = p.read_text(encoding="utf-8")

t = t.replace(
'''            job = JobRepository(
                db
            ).create(

                JobDescription(

                    job_code=parsed.get(
                        "job_code",
                        "",
                    ),

                    designation=parsed.get(
                        "designation",
                        "",
                    ),

                    location=parsed.get(
                        "location",
                        "",
                    ),

                    experience_required=float(
                        parsed.get(
                            "experience_required",
                            0,
                        )
                    ),

                )

            )''',
'''            if hasattr(parsed, "__dict__"):
                parsed_data = parsed.__dict__
            else:
                parsed_data = parsed

            job = JobRepository(
                db
            ).create(

                JobDescription(

                    job_code=parsed_data.get(
                        "job_code",
                        "",
                    ),

                    designation=parsed_data.get(
                        "designation",
                        "",
                    ),

                    location=parsed_data.get(
                        "location",
                        "",
                    ),

                    experience_required=float(
                        parsed_data.get(
                            "experience_required",
                            0,
                        )
                    ),

                )

            )'''
)

t = t.replace(
'''            for skill in parsed.get(
                "skills",
                [],
            ):''',
'''            for skill in parsed_data.get(
                "skills",
                [],
            ):'''
)

t = t.replace(
'''                    len(

                    parsed.get(
                        "skills",
                        [],
                    )

                ),

                "parsed_data": parsed,''',
'''                    len(

                    parsed_data.get(
                        "skills",
                        [],
                    )

                ),

                "parsed_data": parsed_data,''')

p.write_text(t, encoding="utf-8")

print("JD model response compatibility patch applied")
