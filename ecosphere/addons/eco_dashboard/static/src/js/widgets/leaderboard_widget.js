/** @odoo-module **/

import { Component, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class LeaderboardWidget extends Component {
    static template = xml`
        <div class="eco-glass-card h-100">
            <div class="card-header">
                <i class="fa fa-trophy"></i>
                <span t-esc="props.config.title || 'Leaderboard'"/>
            </div>
            <div class="flex-grow-1 overflow-auto">
                <table class="table table-dark table-borderless table-sm">
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Employee</th>
                            <th class="text-end">XP</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>#1</td><td>Sarah Connor</td><td class="text-end text-warning">4,500</td></tr>
                        <tr><td>#2</td><td>John Smith</td><td class="text-end text-warning">3,200</td></tr>
                        <tr><td>#3</td><td>Alice Walker</td><td class="text-end text-warning">2,950</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    `;
}
registry.category("eco_dashboard_widgets").add("leaderboard", LeaderboardWidget);
