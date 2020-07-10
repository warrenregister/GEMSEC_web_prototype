DROP TABLE IF EXISTS desc_files;
DROP TABLE IF EXISTS ngs;

CREATE TABLE ngs(
    file_id TEXT PRIMARY KEY,
    code TEXT references desc_files,
    file_loc TEXT
    );

CREATE TABLE md(
    file_id TEXT PRIMARY KEY,
    code TEXT references desc_files,
    file_loc TEXT
);

CREATE TABLE desc_files(
    code TEXT PRIMARY KEY,
    file_loc TEXT
);

INSERT INTO ngs VALUES ('ngs_0', 'code1_code5', './ngs/ngs1.csv'),
                       ('ngs_1', 'code1_code6', './ngs/ngs1.csv');

INSERT INTO md VALUES ('md_0', 'code2_code3_code5', './ngs/ngs1.csv'),
                      ('md_1', 'code2_code3_code6', './ngs/ngs1.csv'),
                      ('md_2', 'code2_code4_code5', './ngs/ngs1.csv'),
                      ('md_3', 'code2_code4_code6', './ngs/ngs1.csv'),
                      ('md_4', 'code2_code3_code5', './ngs/ngs1.csv');
                      
INSERT INTO desc_files VALUES ('code1', '/Users/warren/Documents/Meta_Data_Site/descriptions/ngs_description.txt'),
                              ('code2', '/Users/warren/Documents/Meta_Data_Site/descriptions/md_description.txt'),
                              ('code3', '/Users/warren/Documents/Meta_Data_Site/descriptions/parameters_A.txt'),
                              ('code4', '/Users/warren/Documents/Meta_Data_Site/descriptions/parameters_B.txt'),
                              ('code5', '/Users/warren/Documents/Meta_Data_Site/descriptions/jackson_frank.txt'),
                              ('code6', '/Users/warren/Documents/Meta_Data_Site/descriptions/warren_register.txt');