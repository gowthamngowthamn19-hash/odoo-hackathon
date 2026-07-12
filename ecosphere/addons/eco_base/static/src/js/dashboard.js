/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

export class EcoDashboard extends Component {
    setup() {
        // Future logic for fetching real data via RPC
    }
}

EcoDashboard.template = "eco_base.Dashboard";

registry.category("actions").add("eco_base.dashboard", EcoDashboard);
