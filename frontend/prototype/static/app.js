const API_BASE = "/api/v1";

const apiStatus = document.querySelector("#apiStatus");
const statusDot = document.querySelector(".status-dot");
const form = document.querySelector("#roomForm");
const button = document.querySelector("#calculateButton");
const message = document.querySelector("#message");

const targets = {
  core: document.querySelector("#coreSummary"),
  execution: document.querySelector("#executionSummary"),
  materials: document.querySelector("#materialSummary"),
  cost: document.querySelector("#costSummary"),
  procurement: document.querySelector("#procurementSummary"),
};

function showMessage(text, type = "success") {
  message.textContent = text;
  message.className = `message ${type}`;
}

function hideMessage() {
  message.className = "message hidden";
  message.textContent = "";
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
        <span class="badge">${item.stage}</span>
        <strong>${item.operation_name}</strong>
        <span>${item.surface_type}</span>
        <span>${item.quantity} ${item.unit}</span>
      </div>
    `)
    .join("");
}

function renderMaterials(data) {
  targets.materials.innerHTML = table(
    ["Материал", "Операция", "Кол-во", "Ед.", "Упаковок"],
    data.items.map((item) => [
      item.material_name,
      item.source_operation_id,
      item.calculated_quantity,
      item.unit,
      item.package_count,
    ])
  );
}

function renderCost(body) {
  const warning = body.warnings?.[0]
    ? `<p><span class="warning-pill">${body.warnings[0].error_code}</span></p>`
    : "";

  targets.cost.innerHTML = `
    ${warning}
    ${table(
      ["Материал", "Упаковок", "Цена", "Итого", "Статус"],
      body.data.items.map((item) => [
        item.material_name,
        item.package_count,
        item.unit_price ?? "—",
        item.total_price ?? "—",
        item.price_status,
      ])
    )}
  `;
}

function renderProcurement(data) {
  targets.procurement.innerHTML = table(
    ["Материал", "Нужно", "Ед.", "Упаковок", "Купить", "Статус"],
    data.items.map((item) => [
      item.material_name,
      item.required_quantity,
      item.unit,
      item.package_count,
      item.purchase_quantity,
      item.price_status,
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

    renderCore(core.data);
    renderExecution(execution.data);
    renderMaterials(materials.data);
    renderCost(cost);
    renderProcurement(procurement.data);

    showMessage("Расчёт успешно выполнен. Данные получены из backend API.");
  } catch (error) {
    showMessage(error.message, "error");
  } finally {
    button.disabled = false;
    button.textContent = "Рассчитать комнату";
  }
});

checkHealth();
