DROP TABLE IF EXISTS halfyearly_exam_marks;

CREATE TABLE halfyearly_exam_marks (
    std_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    std_name TEXT NOT NULL,
    maths INTEGER NOT NULL,
    physics INTEGER NOT NULL,
    coding INTEGER NOT NULL,
    grade INTEGER NOT NULL
);

