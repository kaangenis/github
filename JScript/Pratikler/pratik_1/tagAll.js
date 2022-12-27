// TUTORIAL
// 1. Ir a info del grupo
// 2. Bajar hasta la parte que muestra los participantes
// 3. Entrar en "Ver todos"
// 4. Abrir herramientas de desarrollador y pegar este script en la consola

// Constants declared with 'let' to prevent errors if executing script several times
let MAX_CONSECUTIVE_SAME_SIZES = 3;
let MEMBER_LIST_SELECTOR =
  "#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div._3Bc7H.g0rxnol2.thghmljt.p357zi0d.rjo8vgbg.ggj6brxn.f8m0rgwh.gfz4du6o.ag5g9lrv.bs7a17vp.ov67bkzj > div > div > div > div div div div._3OvU8 div._3vPI2 div span";
let SCROLL_PIXELS = 500;
let SCROLL_ELEM_CLASSNAME =
  "_3Bc7H g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o ag5g9lrv bs7a17vp ov67bkzj";

let members = new Set();
let prevMemberSize = 0;
let consecutiveSameSizes = 0;
let scrapingIntervalID = null;

let getMemberElems = () => {
  return document.querySelectorAll(MEMBER_LIST_SELECTOR);
};

let addElemsTextToMembers = (membersList) =>
  membersList.forEach((elem) => members.add(elem.innerText));

let scrollDown = () => {
  document
    .getElementsByClassName(SCROLL_ELEM_CLASSNAME)[0]
    .scrollBy(0, SCROLL_PIXELS);
};

let updateConsecutiveSameSizes = (memberSize) => {
  if (prevMemberSize === memberSize) {
    consecutiveSameSizes++;
  } else {
    consecutiveSameSizes = 0;
  }
  prevMemberSize = memberSize;
};

let stopScraping = () => {
  console.log("Stopping scraper...");
  clearInterval(scrapingIntervalID);
};

let giveOutput = () => {
  let membersArray = Array.from(members);
  let text = "@" + membersArray.join("\n@");
  console.log(text);
  console.log("Size: ", members.size);
};

let scrapeMembers = () => {
  let memberElems = getMemberElems();
  addElemsTextToMembers(memberElems);
  scrollDown();
  let currentMemberSize = members.size;

  updateConsecutiveSameSizes(currentMemberSize);

  let shouldStop = consecutiveSameSizes > MAX_CONSECUTIVE_SAME_SIZES;
  if (shouldStop) {
    stopScraping();
    giveOutput();
  }
};

scrapingIntervalID = setInterval(scrapeMembers, 1000);
