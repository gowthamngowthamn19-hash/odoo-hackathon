/** @odoo-module **/

import { Component, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class NotificationWidget extends Component {
    static template = xml`
        <div class="eco-glass-card h-100">
            <div class="card-header">
                <i class="fa fa-bell text-warning"></i>
                <span t-esc="props.config.title || 'Notifications'"/>
            </div>
            <div class="flex-grow-1">
                <div class="alert alert-warning py-2 mb-2">
                    Pending Compliance Audit for IT Dept
                </div>
            </div>
        </div>
    `;
}
registry.category("eco_dashboard_widgets").add("notification", NotificationWidget);
