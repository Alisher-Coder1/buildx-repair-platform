const API_BASE = "/api/v1";

const apiStatus = document.querySelector("#apiStatus");
const statusDot = document.querySelector(".status-dot");
const form = document.querySelector("#roomForm");
const button = document.querySelector("#calculateButton");
const message = document.querySelector("#message");

const targets = {
  overview: document.querySelector("#resultOverview"),
  core: document.querySelector("#coreSummary"),
  execution: document.querySelector("#executionSummary"),
  materials: document.querySelector("#materialSummary"),
  cost: document.querySelector("#costSummary"),
  procurement: document.querySelector("#procurementSummary"),
};

const dictionaries = {
  stage: {
    STG_PREP: "Подготовка",
    STG_WATERPROOF: "Гидроизоляция",
    STG_ROUGH: "Черновой этап",
    STG_FINISH: "Чистовой этап",
  },
  surface: {
    FLOOR: "Пол",
    WALLS: "Стены",
    CEILING: "Потолок",
  },
  unit: {
    M2: "м²",
    M_LINEAR: "м.пог.",
    LITER: "л",
    KG: "кг",
    PCS: "шт.",
    ROLL: "рулон",
    PACKAGE: "уп.",
  },
  material: {
    Primer: "Грунтовка",
    Waterproofing: "Гидроизоляция",
    "Plaster mix": "Штукатурная смесь",
    "Ceiling paint": "Краска для потолка",
    "Tile adhesive": "Плиточный клей",
    Grout: "Затирка",
    "Porcelain tile": "Керамогранит",
  },
  operation: {
    OPR_FLOOR_PREP: "Подготовка поверхности пола",
    OPR_WALL_PREP: "Подготовка поверхности стен",
    OPR_CEILING_PREP: "Подготовка поверхности потолка",
    OPR_FLOOR_WATERPROOFING: "Гидроизоляция пола",
    OPR_WALL_WATERPROOFING: "Гидроизоляция стен",
    OPR_WALL_PLASTER: "Штукатурка стен",
    OPR_WALL_PUTTY: "Шпаклёвка стен",
    OPR_WALL_PAINT: "Покраска стен",
    OPR_WALL_WALLPAPER: "Поклейка обоев",
    OPR_WALL_TILE_INSTALL: "Укладка плитки на стены",
    OPR_CEILING_PAINT: "Покраска потолка",
    OPR_FLOOR_TILE_INSTALL: "Укладка плитки на пол",
    OPR_FLOOR_LAMINATE_INSTALL: "Укладка ламината",
    OPR_FLOOR_LINOLEUM_INSTALL: "Укладка линолеума",
    OPR_FLOOR_SELF_LEVELING: "Наливной пол",
    OPR_SKIRTING_INSTALL: "Монтаж плинтуса",
  },
  priceStatus: {
    MISSING_PRICE: "Цена не указана",
  },
};

function label(group, value) {
  return dictionaries[group]?.[value] ?? value;
}

function showMessage(text, type = "success") {
  message.textContent = text;
  message.className = `message ${type}`;
}

function hideMessage() {
  message.className = "message hidden";
  message.textContent = "";
}

function humanError(error) {
  const text = String(error.message || error);

  if (text.includes("Failed to fetch")) {
    return "Frontend не смог подключиться к backend. Проверьте, что сервер запущен через uvicorn.";
  }

  if (text.includes("ERR_OUT_OF_RANGE")) {
    return "Размеры комнаты вне допустимого диапазона. Проверьте длину, ширину и высоту.";
  }

  if (text.includes("ERR_UNSUPPORTED_COVERING")) {
    return "Выбрано покрытие, которого пока нет в правилах Prototype v0.1.";
  }

  if (text.includes("ERR_ARTIFACT")) {
    return "Ошибка в JSON artifacts. Backend не смог безопасно выполнить расчёт.";
  }

  return text;
}

async function api(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  const body = await response.json();

  if (!response.ok || body.success === false) {
    const detail = body.detail || body;
    const error = detail.errors?.[0] || body.errors?.[0];
    const text = error
      ? `${error.error_code}: ${error.message}`
      : `HTTP ${response.status}`;
    throw new Error(text);
  }

  return body;
}

function asNumber(value) {
  return Number.parseFloat(value);
}

function formPayload(formData) {
  return {
    project_name: formData.get("project_name"),
    room_name: formData.get("room_name"),
    length_m: asNumber(formData.get("length_m")),
    width_m: asNumber(formData.get("width_m")),
    height_m: asNumber(formData.get("height_m")),
    zone: formData.get("zone"),
    floor_covering: formData.get("floor_covering"),
    wall_covering: formData.get("wall_covering"),
    ceiling_covering: formData.get("ceiling_covering"),
  };
}

function renderOverview({ execution, materials, cost, procurement }) {
  const operationCount = execution.data.operations.length;
  const materialRows = materials.data.items.length;
  const packageCount = procurement.data.items.reduce((sum, item) => sum + item.package_count, 0);
  const missingPrices = cost.data.items.filter((item) => item.price_status === "MISSING_PRICE").length;

  targets.overview.innerHTML = `
    <div class="overview-card">
      <strong>${operationCount}</strong>
      <span>работ</span>
    </div>
    <div class="overview-card">
      <strong>${materialRows}</strong>
      <span>строк материалов</span>
    </div>
    <div class="overview-card">
      <strong>${packageCount}</strong>
      <span>упаковок к закупке</span>
    </div>
    <div class="overview-card warning">
      <strong>${missingPrices}</strong>
      <span>цен нужно заполнить</span>
    </div>
  `;
}

function renderCore(data) {
  const g = data.geometry;
  targets.core.innerHTML = `
    <div class="metric-card"><strong>${g.floor_area_m2}</strong><span>Площадь пола, м²</span></div>
    <div class="metric-card"><strong>${g.ceiling_area_m2}</strong><span>Площадь потолка, м²</span></div>
    <div class="metric-card"><strong>${g.wall_area_m2}</strong><span>Площадь стен, м²</span></div>
    <div class="metric-card"><strong>${g.perimeter_m}</strong><span>Периметр, м.пог.</span></div>
  `;
}

function renderExecution(data) {
  if (!data.operations.length) {
    targets.execution.innerHTML = `<div class="empty">Нет операций.</div>`;
    return;
  }

  targets.execution.innerHTML = data.operations
    .map((item) => `
      <div class="operation-row">
        <span class="badge">${label("stage", item.stage)}</span>
        <strong>${label("operation", item.operation_id)}</strong>
        <span>${label("surface", item.surface_type)}</span>
        <span>${item.quantity} ${label("unit", item.unit)}</span>
      </div>
    `)
    .join("");
}

function renderMaterials(data) {
  targets.materials.innerHTML = table(
    ["Материал", "Операция", "Кол-во", "Ед.", "Упаковок"],
    data.items.map((item) => [
      label("material", item.material_name),
      label("operation", item.source_operation_id),
      item.calculated_quantity,
      label("unit", item.unit),
      item.package_count,
    ])
  );
}

function renderCost(body) {
  const warning = body.warnings?.[0]
    ? `
      <div class="explain-warning">
        <span class="warning-pill">${body.warnings[0].error_code}</span>
        <p>
          Цены пока не заполнены. Это не ошибка расчёта: backend уже посчитал материалы
          и упаковки, а стоимость появится после добавления прайс-листа.
        </p>
      </div>
    `
    : "";

  targets.cost.innerHTML = `
    ${warning}
    ${table(
      ["Материал", "Упаковок", "Цена", "Итого", "Статус"],
      body.data.items.map((item) => [
        label("material", item.material_name),
        item.package_count,
        item.unit_price ?? "—",
        item.total_price ?? "—",
        label("priceStatus", item.price_status),
      ])
    )}
  `;
}

function renderProcurement(data) {
  targets.procurement.innerHTML = table(
    ["Материал", "Нужно", "Ед.", "Упаковок", "Купить", "Статус"],
    data.items.map((item) => [
      label("material", item.material_name),
      item.required_quantity,
      label("unit", item.unit),
      item.package_count,
      item.purchase_quantity,
      label("priceStatus", item.price_status),
    ])
  );
}

function table(headers, rows) {
  if (!rows.length) {
    return `<div class="empty">Нет данных.</div>`;
  }

  return `
    <table>
      <thead>
        <tr>${headers.map((h) => `<th>${h}</th>`).join("")}</tr>
      </thead>
      <tbody>
        ${rows
          .map((row) => `<tr>${row.map((cell) => `<td>${cell}</td>`).join("")}</tr>`)
          .join("")}
      </tbody>
    </table>
  `;
}

async function checkHealth() {
  try {
    const body = await api("/health");
    apiStatus.textContent = `${body.data.status} · ${body.data.version}`;
    statusDot.classList.add("ok");
  } catch (error) {
    apiStatus.textContent = "Недоступен";
    statusDot.classList.add("error");
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  hideMessage();
  button.disabled = true;
  button.textContent = "Считаем...";

  try {
    const formData = new FormData(form);
    const payload = formPayload(formData);

    const project = await api("/projects", {
      method: "POST",
      body: JSON.stringify({ project_name: payload.project_name }),
    });

    const projectId = project.data.project_id;

    const room = await api(`/projects/${projectId}/rooms`, {
      method: "POST",
      body: JSON.stringify({
        room_name: payload.room_name,
        length_m: payload.length_m,
        width_m: payload.width_m,
        height_m: payload.height_m,
        zone: payload.zone,
        floor_covering: payload.floor_covering,
        wall_covering: payload.wall_covering,
        ceiling_covering: payload.ceiling_covering,
      }),
    });

    const roomId = room.data.room_id;

    const [core, execution, materials, cost, procurement] = await Promise.all([
      api(`/rooms/${roomId}/core-summary`),
      api(`/rooms/${roomId}/execution-summary`),
      api(`/rooms/${roomId}/material-consumption-summary`),
      api(`/rooms/${roomId}/cost-summary`),
      api(`/rooms/${roomId}/procurement-summary`),
    ]);

    renderOverview({ execution, materials, cost, procurement });
    renderCore(core.data);
    renderExecution(execution.data);
    renderMaterials(materials.data);
    renderCost(cost);
    renderProcurement(procurement.data);

    showMessage("Расчёт успешно выполнен. Данные получены из backend API.");
  } catch (error) {
    showMessage(humanError(error), "error");
  } finally {
    button.disabled = false;
    button.textContent = "Рассчитать комнату";
  }
});

checkHealth();
