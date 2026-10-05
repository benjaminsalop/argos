// Thin shell: registers commands that call the `argos` CLI and render outputs in a webview.
// Campaign YAML validation comes from the JSON Schema declared in package.json (copy of configs/schema/campaign.schema.json).
export function activate(): void {
  // TODO: register argos.runEnrich, argos.openWeights, argos.showResults
}

export function deactivate(): void {}
