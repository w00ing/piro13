const input = document.querySelector("#passwordInput");
const addBtn = document.querySelector(".add");

const onAddClick = () => {
  console.log(input.value);
  if (input.value === "1234") {
    const newCityName = document.querySelector(".cityInput").value;
    const newElem = document.createElement("li");
    newElem.innerText = newCityName;
    const cityList = document.querySelector("ul");
    cityList.appendChild(newElem);
  } else {
    console.log("No");
  }
};

addBtn.addEventListener("click", onAddClick);
