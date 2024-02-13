# delete old column
ALTER TABLE read_01
DROP COLUMN IF EXISTS spd_01

# add fresh column
ALTER TABLE read_01
ADD COLUMN spd_01 smallint 

# set everything to 0
UPDATE read_01
SET spd_01 = 0;

# set cards pulled to 1
UPDATE read_01
SET spd_01 = 1
WHERE