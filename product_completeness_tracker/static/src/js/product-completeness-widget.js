/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

class CompletenessProgress extends Component {
    static template = "product_completeness_tracker.CompletenessProgress";
    static props = { ...standardFieldProps };

    get score() {
        return this.props.record.data[this.props.name] ?? 0;
    }

    get barColor() {
        const s = this.score;
        if (s >= 80) return "#22c55e";
        if (s >= 50) return "#f59e0b";
        return "#ef4444";
    }
}

registry.category("fields").add("completeness_progress", {
    component: CompletenessProgress,
    supportedTypes: ["float"],
});
