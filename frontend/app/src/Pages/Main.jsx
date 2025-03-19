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
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions
} from "@mui/material";
import { useState } from "react";
import axios from "axios";

const Main = () => {
  /* API CALLS */
  const BASE_API_URI = "http://localhost:8080"

  function getClosestStation() {
    const lat = gpsLocation.split("/")[0];
    const lon = gpsLocation.split("/")[1];
    const max_distance = 5;
  
    axios.get(`${BASE_API_URI}/data/get_closest_stations/`, {
      params: {
        lat: lat,  // Latitude
        lon: lon,  // Longitude
        max_distance: max_distance  // Distance max
      },
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      setNearestAllData(response.data[0]);
      setNearestAllData2(response.data[1]);
  
      setNearestID(nearestAllData["id"]);
      setNearestName(nearestAllData["name"]);
      setLatitude(nearestAllData["latitude"] + " / " + nearestAllData["longitude"]);
      setDistance(nearestAllData["distance"]);
      setTown(nearestAllData["town"]);
  
      setNearestId2(nearestAllData2["id"]);
      setNearestName2(nearestAllData2["name"]);
      setLatitude2(nearestAllData2["latitude"] + " / " + nearestAllData2["longitude"]);
      setDistance2(nearestAllData2["distance"]);
      setTown2(nearestAllData2["town"]);
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });
  }


  /* First Box */
  const [gpsLocation, setGpsLocation] = useState("");
  const [countryName, setCountryName] = useState("");
  // const [movingMeans, setMovingMeans] = useState("by feet");
  const [predictiveResearchPeriod, setPredictiveResearchPeriod] =
    useState("current");

    const [cleanWater, setCleanWater] = useState({
      name: "Clean water",
      checked: false,
    });
    
    const [uncleanWater, setUncleanWater] = useState({
      name: "Unclean water",
      checked: false,
    });
    
    const [unknown, setUnknown] = useState({
      name: "Unknown",
      checked: false,
    });

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
  const [open, setOpen] = useState(false);

  const [nearestAllData, setNearestAllData] = useState({});
  const [nearestName, setNearestName] = useState("");
  const [nearestID, setNearestID] = useState();
  const [waterQuality, setWaterQuality] = useState("");
  const [waterType, setWaterType] = useState("");
  const [town, setTown] = useState("");
  const [latitudelongitude, setLatitude] = useState("");
  const [distance, setDistance] = useState("");

  const [nearestAllData2, setNearestAllData2] = useState({});
  const [nearestName2, setNearestName2] = useState("");
  const [nearestId2, setNearestId2] = useState();
  const [waterQuality2, setWaterQuality2] = useState("");
  const [waterType2, setWaterType2] = useState("");
  const [town2, setTown2] = useState("");
  const [latitude2, setLatitude2] = useState("");
  const [distance2, setDistance2] = useState("");

  /* End second box */

  /* Dialog */
  function openDialog(datas)
  {
    set_station_id(datas["station_id"]);
    set_sample_date(datas["sample_date"]);
    set_longitude(datas["longitude"]);
    set_latitude(datas["latitude"]);
    set_boron_value(datas["boron_value"]);
    set_cadmium_value(datas["cadmium_value"]);
    set_oxygen_demand_value(datas["oxygen_demand_value"]);
    set_sulfur_value(datas["sulfur_value"]);
    set_silver_value(datas["silver_value"]);
    set_manganese_value(datas["manganese_value"]);
    set_electrical_conductance_value(datas["electrical_conductance_value"]);
    set_selenium_value(datas["selenium_value"]);
    set_water_value(datas["water_value"]);
    set_nickel_value(datas["nickel_value"]);
    set_cyanide_value(datas["cyanide_value"]);
    set_alkalinity_value(datas["alkalinity_value"]);
    set_copper_value(datas["copper_value"]);
    set_sodium_value(datas["sodium_value"]);
    set_mercury_value(datas["mercury_value"]);
    set_magnesium_value(datas["magnesium_value"]);
    set_arsenic_value(datas["arsenic_value"]);
    set_pH_value(datas["pH_value"]);
    set_oxidized_nitrogen_value(datas["oxidized_nitrogen_value"]);
    set_iron_value(datas["iron_value"]);
    set_optical_value(datas["optical_value"]);
    set_potassium_value(datas["potassium_value"]);
    set_calcium_value(datas["calcium_value"]);
    set_hardness_value(datas["hardness_value"]);
    set_chloride_value(datas["chloride_value"]);
    set_lead_value(datas["lead_value"]);
    set_other_nitrogen_value(datas["other_nitrogen_value"]);
    set_chromium_value(datas["chromium_value"]);
    set_zinc_value(datas["zinc_value"]);

    setOpen(true);
  }

  const [station_id, set_station_id] = useState(null);
  const [sample_date, set_sample_date] = useState(null);
  const [longitude, set_longitude] = useState(null);
  const [latitude, set_latitude] = useState(null);
  const [boron_value, set_boron_value] = useState(null);
  const [cadmium_value, set_cadmium_value] = useState(null);
  const [oxygen_demand_value, set_oxygen_demand_value] = useState(null);
  const [sulfur_value, set_sulfur_value] = useState(null);
  const [silver_value, set_silver_value] = useState(null);
  const [manganese_value, set_manganese_value] = useState(null);
  const [electrical_conductance_value, set_electrical_conductance_value] = useState(null);
  const [selenium_value, set_selenium_value] = useState(null);
  const [water_value, set_water_value] = useState(null);
  const [nickel_value, set_nickel_value] = useState(null);
  const [cyanide_value, set_cyanide_value] = useState(null);
  const [alkalinity_value, set_alkalinity_value] = useState(null);
  const [copper_value, set_copper_value] = useState(null);
  const [sodium_value, set_sodium_value] = useState(null);
  const [mercury_value, set_mercury_value] = useState(null);
  const [magnesium_value, set_magnesium_value] = useState(null);
  const [arsenic_value, set_arsenic_value] = useState(null);
  const [pH_value, set_pH_value] = useState(null);
  const [oxidized_nitrogen_value, set_oxidized_nitrogen_value] = useState(null);
  const [iron_value, set_iron_value] = useState(null);
  const [optical_value, set_optical_value] = useState(null);
  const [potassium_value, set_potassium_value] = useState(null);
  const [calcium_value, set_calcium_value] = useState(null);
  const [hardness_value, set_hardness_value] = useState(null);
  const [chloride_value, set_chloride_value] = useState(null);
  const [lead_value, set_lead_value] = useState(null);
  const [other_nitrogen_value, set_other_nitrogen_value] = useState(null);
  const [chromium_value, set_chromium_value] = useState(null);
  const [zinc_value, set_zinc_value] = useState(null);

  var textFieldsObjects = [
    { label: "Sample Date", name: "sample_date", state: sample_date, setter: set_sample_date },
    { label: "Longitude", name: "longitude", state: longitude, setter: set_longitude },
    { label: "Latitude", name: "latitude", state: latitude, setter: set_latitude },
    { label: "Boron Value", name: "boron_value", state: boron_value, setter: set_boron_value },
    { label: "Cadmium Value", name: "cadmium_value", state: cadmium_value, setter: set_cadmium_value },
    { label: "Oxygen Demand Value", name: "oxygen_demand_value", state: oxygen_demand_value, setter: set_oxygen_demand_value },
    { label: "Sulfur Value", name: "sulfur_value", state: sulfur_value, setter: set_sulfur_value },
    { label: "Silver Value", name: "silver_value", state: silver_value, setter: set_silver_value },
    { label: "Manganese Value", name: "manganese_value", state: manganese_value, setter: set_manganese_value },
    { label: "Electrical Conductance", name: "electrical_conductance_value", state: electrical_conductance_value, setter: set_electrical_conductance_value },
    { label: "Selenium Value", name: "selenium_value", state: selenium_value, setter: set_selenium_value },
    { label: "Water Value", name: "water_value", state: water_value, setter: set_water_value },
    { label: "Nickel Value", name: "nickel_value", state: nickel_value, setter: set_nickel_value },
    { label: "Cyanide Value", name: "cyanide_value", state: cyanide_value, setter: set_cyanide_value },
    { label: "Alkalinity Value", name: "alkalinity_value", state: alkalinity_value, setter: set_alkalinity_value },
    { label: "Copper Value", name: "copper_value", state: copper_value, setter: set_copper_value },
    { label: "Sodium Value", name: "sodium_value", state: sodium_value, setter: set_sodium_value },
    { label: "Mercury Value", name: "mercury_value", state: mercury_value, setter: set_mercury_value },
    { label: "Magnesium Value", name: "magnesium_value", state: magnesium_value, setter: set_magnesium_value },
    { label: "Arsenic Value", name: "arsenic_value", state: arsenic_value, setter: set_arsenic_value },
    { label: "pH Value", name: "pH_value", state: pH_value, setter: set_pH_value },
    { label: "Oxidized Nitrogen", name: "oxidized_nitrogen_value", state: oxidized_nitrogen_value, setter: set_oxidized_nitrogen_value },
    { label: "Iron Value", name: "iron_value", state: iron_value, setter: set_iron_value },
    { label: "Optical Value", name: "optical_value", state: optical_value, setter: set_optical_value },
    { label: "Potassium Value", name: "potassium_value", state: potassium_value, setter: set_potassium_value },
    { label: "Calcium Value", name: "calcium_value", state: calcium_value, setter: set_calcium_value },
    { label: "Hardness Value", name: "hardness_value", state: hardness_value, setter: set_hardness_value },
    { label: "Chloride Value", name: "chloride_value", state: chloride_value, setter: set_chloride_value },
    { label: "Lead Value", name: "lead_value", state: lead_value, setter: set_lead_value },
    { label: "Other Nitrogen Value", name: "other_nitrogen_value", state: other_nitrogen_value, setter: set_other_nitrogen_value },
    { label: "Chromium Value", name: "chromium_value", state: chromium_value, setter: set_chromium_value },
    { label: "Zinc Value", name: "zinc_value", state: zinc_value, setter: set_zinc_value },
  ]

  async function sendModifications()
  {
    await axios.post(BASE_API_URI + "/contribute/", {
      station_id,
      sample_date,
      longitude,
      latitude,
      boron_value,
      cadmium_value,
      oxygen_demand_value,
      sulfur_value,
      silver_value,
      manganese_value,
      electrical_conductance_value,
      selenium_value,
      water_value,
      nickel_value,
      cyanide_value,
      alkalinity_value,
      copper_value,
      sodium_value,
      mercury_value,
      magnesium_value,
      arsenic_value,
      pH_value,
      oxidized_nitrogen_value,
      iron_value,
      optical_value,
      potassium_value,
      calcium_value,
      hardness_value,
      chloride_value,
      lead_value,
      other_nitrogen_value,
      chromium_value,
      zinc_value
    });
    setOpen(false);
  }
  /* End Dialog */

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
              <FormControlLabel
                  control={
                    <Checkbox
                      checked={cleanWater.checked}
                      onChange={(e) =>
                        setCleanWater({ name: "Clean water", checked: e.target.checked})
                      }
                    />
                  }
                  label={cleanWater.name}
                />
                <FormControlLabel
                  control={
                    <Checkbox
                      checked={uncleanWater.checked}
                      onChange={(e) =>
                        setUncleanWater({ name: "Unclean water", checked: e.target.checked})
                      }
                    />
                  }
                  label={uncleanWater.name}
                />
                <FormControlLabel
                  control={
                    <Checkbox
                      checked={unknown.checked}
                      onChange={(e) =>
                        setUnknown({ name: "Unknown", checked: e.target.checked})
                      }
                    />
                  }
                  label={unknown.name}
                />

            </FormGroup>
          </Stack>

          {/* <Stack direction="column" alignItems="start" sx={{ margin: "10px" }}>
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
          </Stack> */}

          <Stack direction="column" alignItems="start" sx={{ margin: "10px" }}>
            {/* <FormControl>
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
            </FormControl> */}

            <br />
            <Button variant="contained" color="success" onClick={() => getClosestStation()}>
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
                  <Button variant="contained" color="error" onClick={() => openDialog(nearestAllData)}>
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
                  value={latitudelongitude}
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
                  <Button variant="contained" color="error" onClick={() => openDialog(nearestAllData2)}>
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

      <Dialog open={open} onClose={(() => StereoPannerNode(false))}>
        <DialogTitle>Edit water point datas</DialogTitle>
        <DialogContent>
            <Stack direction="column" spacing={2}>
              {
                textFieldsObjects.map(({label, state, setter}) => (
                  <Stack key={label} direction="column" alignItems="start" width="90%">
                    <Typography sx={{ fontWeight: "bold"}}>{label}</Typography>
                    <TextField sx={{ width: "100%", background: "white"}} value={state} onChange={(e) => setter(e.target.value)} />
                  </Stack>
                ))
              }
            </Stack>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => sendModifications()} color="success" />
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default Main;
