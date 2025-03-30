import React from "react";
import {
  Box,
  Typography,
  Stack,
  TextField,
  FormControl,
  FormControlLabel,
  FormGroup,
  FormLabel,
  Checkbox,
  Radio,
  RadioGroup,
  Button,
} from "@mui/material";
import { useState } from "react";

const Main = () => {
  /* First Box */
  const [gpsLocation, setGpsLocation] = useState("");
  const [countryName, setCountryName] = useState("");
  const [movingMeans, setMovingMeans] = useState("by feet");
  const [predictiveResearchPeriod, setPredictiveResearchPeriod] =
    useState("current");

  const [waterQualityCriteria, setWaterQualityCriteria] = useState([
    {
      name: "Clean water",
      checked: false,
    },
    {
      name: "Unclean water",
      checked: false,
    },
    {
      name: "Unknown",
      checked: false,
    },
  ]);

  function changeQuality(isChecked, label) {
    console.log(label + " " + isChecked);
    let temp = waterQualityCriteria;

    for (let i = 0; i < temp.length; i++) {
      if (temp[i].name === label) temp[i].checked = isChecked;
    }
    setWaterQualityCriteria(temp);
  }
  /* End First Box */

  /* Second Box */

  const [nearestName, setNearestName] = useState("");
  const [waterQuality, setWaterQuality] = useState("");
  const [waterType, setWaterType] = useState("");
  const [town, setTown] = useState("");
  const [latitude, setLatitude] = useState("");
  const [distance, setDistance] = useState("");

  const [nearestName2, setNearestName2] = useState("");
  const [waterQuality2, setWaterQuality2] = useState("");
  const [waterType2, setWaterType2] = useState("");
  const [town2, setTown2] = useState("");
  const [latitude2, setLatitude2] = useState("");
  const [distance2, setDistance2] = useState("");

  /* End second box */

  return (
    <div>
      <Stack alignItems="center" direction="column">
        <Typography variant="h3">HydroReport by</Typography>
      </Stack>

      <Stack direction="Row" sx={{ margin: "20px" }} minHeight="90vh">
        <Box
          sx={{
            background: "#d7e5f7",
            width: "100%",
            minheight: "90vh",
            borderRadius: "10px",
          }}
        >
          <Stack
            direction="column"
            sx={{ margin: "10px" }}
            alignItems="start"
            width="100%"
          >
            <Typography variant="h5" sx={{ fontWeight: "bold" }}>
              LOCATION TO START FROM
            </Typography>
            <br />

            <Stack direction="column" alignItems="start" width="96%">
              <Typography sx={{ fontWeight: "bold" }}>GPS Location</Typography>
              <TextField
                sx={{ width: "100%", background: "white" }}
                label="egs 13.5115963, 2.1253854"
                value={gpsLocation}
                onChange={(e) => setGpsLocation(e.target.value)}
              />
            </Stack>

            <Stack direction="column" alignItems="start" width="96%">
              <Typography sx={{ fontWeight: "bold" }}>
                or Enter a Country / Town name
              </Typography>
              <TextField
                sx={{ width: "100%", background: "white" }}
                label="egs NIGER / Niamery"
                value={countryName}
                onChange={(e) => setCountryName(e.target.value)}
              />
            </Stack>
            <br />

            <FormGroup>
              <FormLabel>Water quality criteria</FormLabel>
              {waterQualityCriteria.map((element) => (
                <FormControlLabel
                  key={element.name}
                  control={
                    <Checkbox
                      checked={element.checked}
                      onChange={(e) =>
                        changeQuality(e.target.checked, element.name)
                      }
                    />
                  }
                  label={element.name}
                />
              ))}
            </FormGroup>
          </Stack>

          <Stack direction="column" alignItems="start" sx={{ margin: "10px" }}>
            <FormControl>
              <FormLabel id="demo-radio-buttons-group-label">
                Moving means
              </FormLabel>
              <RadioGroup
                aria-labelledby="demo-radio-buttons-group-label"
                defaultValue={movingMeans}
                name="radio-buttons-group"
              >
                <FormControlLabel
                  value="by feet"
                  control={<Radio />}
                  label="by feet"
                  onClick={(e) => setMovingMeans(e.target.value)}
                />
                <FormControlLabel
                  value="by bike"
                  control={<Radio />}
                  label="by bike"
                  onClick={(e) => setMovingMeans(e.target.value)}
                />
                <FormControlLabel
                  value="by car"
                  control={<Radio />}
                  label="by car"
                  onClick={(e) => setMovingMeans(e.target.value)}
                />
              </RadioGroup>
            </FormControl>
          </Stack>

          <Stack direction="column" alignItems="start" sx={{ margin: "10px" }}>
            <FormControl>
              <FormLabel id="demo-radio-buttons-group-label">
                Predictive research period
              </FormLabel>
              <RadioGroup
                aria-labelledby="demo-radio-buttons-group-label"
                defaultValue={predictiveResearchPeriod}
                name="radio-buttons-group"
              >
                <FormControlLabel
                  value="current"
                  control={<Radio />}
                  label="current"
                  onClick={(e) => setPredictiveResearchPeriod(e.target.value)}
                />
                <FormControlLabel
                  value="short-term"
                  label="short-term"
                  control={<Radio />}
                  onClick={(e) => setPredictiveResearchPeriod(e.target.value)}
                />
                <FormControlLabel
                  value="medium-term"
                  label="medium-term"
                  control={<Radio />}
                  onClick={(e) => setPredictiveResearchPeriod(e.target.value)}
                />
                <FormControlLabel
                  value="long-term"
                  label="long-term"
                  control={<Radio />}
                  onClick={(e) => setPredictiveResearchPeriod(e.target.value)}
                />
              </RadioGroup>
            </FormControl>

            <br />
            <Button variant="contained" color="success">
              SEARCH FOR WATER
            </Button>
          </Stack>
        </Box>

        <Box sx={{ width: "5vw" }} />
        <Box
          sx={{
            background: "white",
            width: "100%",
            minHeight: "90vh",
            borderRadius: "10px",
          }}
        >
          <Stack direction="column" sx={{ margin: "10px" }} alignItems="start">
            <Typography variant="h5" sx={{ fontWeight: "bold" }}>
              RESULTS
            </Typography>
            <br />
            <Stack
              direction="column"
              sx={{
                margin: "10px",
                background: "#f2f4f8",
                borderRadius: "10px",
              }}
              alignItems="start"
              width="96%"
            >
              <Stack
                direction="column"
                sx={{ margin: "10px" }}
                alignItems="start"
                width="95%"
                spacing={2}
              >
                <Stack
                  direction="row"
                  width="100%"
                  spacing="auto"
                  alignItems="center"
                >
                  <Typography sx={{ fontWeight: "bold" }}>
                    Nearest watering spot
                  </Typography>
                  <Button variant="contained" color="error">
                    Edit data
                  </Button>
                </Stack>
                <TextField
                  {..."disabled"}
                  sx={{ width: "100%", background: "white" }}
                  label="Name (if any)"
                  value={nearestName}
                  onChange={(e) => setNearestName(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Water Quality"
                  value={waterQuality}
                  onChange={(e) => setWaterQuality(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Water Type"
                  value={waterType}
                  onChange={(e) => setWaterType(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Town / Area"
                  value={town}
                  onChange={(e) => setTown(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Latitude / Longitude"
                  value={latitude}
                  onChange={(e) => setLatitude(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Distance / Direction"
                  value={distance}
                  onChange={(e) => setDistance(e.target.value)}
                />
              </Stack>
            </Stack>
            <Stack
              direction="column"
              sx={{
                margin: "10px",
                background: "#f2f4f8",
                borderRadius: "10px",
              }}
              alignItems="start"
              width="96%"
            >
              <Stack
                direction="column"
                sx={{ margin: "10px" }}
                alignItems="start"
                width="95%"
                spacing={2}
              >
                <Stack
                  direction="row"
                  width="100%"
                  spacing="auto"
                  alignItems="center"
                >
                  <Typography sx={{ fontWeight: "bold" }}>
                    Second watering spot
                  </Typography>
                  <Button variant="contained" color="error">
                    Edit data
                  </Button>
                </Stack>
                <TextField
                  sx={{ width: "100%", height: "50%", background: "white" }}
                  label="Name (if any)"
                  value={nearestName2}
                  onChange={(e) => setNearestName2(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Water Quality"
                  value={waterQuality2}
                  onChange={(e) => setWaterQuality2(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Water Type"
                  value={waterType2}
                  onChange={(e) => setWaterType2(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Town / Area"
                  value={town2}
                  onChange={(e) => setTown2(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Latitude / Longitude"
                  value={latitude2}
                  onChange={(e) => setLatitude2(e.target.value)}
                />
                <TextField
                  sx={{ width: "100%", background: "white" }}
                  label="Distance / Direction"
                  value={distance2}
                  onChange={(e) => setDistance2(e.target.value)}
                />
              </Stack>
            </Stack>
          </Stack>

          <Stack
            direction="row"
            width="93%"
            sx={{ marginLeft: "20px", marginBottom: "20px" }}
            spacing="auto"
          >
            <Button variant="contained" color="success">
              All results list
            </Button>
            <Button variant="contained" color="success">
              Generate Map
            </Button>
            <Button variant="contained" color="success">
              Generate Poster
            </Button>
          </Stack>
        </Box>
      </Stack>
    </div>
  );
};

export default Main;
