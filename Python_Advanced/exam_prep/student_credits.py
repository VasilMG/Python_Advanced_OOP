def students_credits(*args):
    courses = {}
    total_sum = 0
    for item in args:
        the_course , *values = item.split('-')
        the_credits, max_points, current_points = [int(x) for x in values]
        diyan_credits = (current_points / max_points) * the_credits
        courses[the_course] = diyan_credits
        total_sum += diyan_credits

    final_courses = [f"{k} - {float(v):.1f}" for k, v in sorted(courses.items(), key= lambda x: -x[1])]
    final_score = sum(courses.values())
    credits_needed = 240 - total_sum
    negative_message = f"Diyan needs {credits_needed:.1f} credits more for a diploma."
    positive_message = f"Diyan gets a diploma with {final_score:.1f} credits."
    if final_score < 240:
        return negative_message + '\n' + '\n'.join(final_courses)
    else:
        return positive_message + '\n' + '\n'.join(final_courses)



print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)